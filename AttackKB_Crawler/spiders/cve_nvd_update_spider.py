import scrapy
import re
from datetime import datetime
from attackKB_crawler.items.cve_nvd_items import CVEItem

class NVDCVEUpdateClass(scrapy.Spider):

    name = 'Update_CVE_NVD'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/full_listing.cfm']
    custom_settings = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            #'attackKB_crawler.pipelines.cve_nvd_pipelines.NVD_CVE_MySQLStorePipeline': 932,
            #'attackKB_crawler.pipelines.cve_nvd_pipelines.NVDCVEUpdateJsonWriterPipeline': 900,
        },
    }
    xpath = {
        "YearList": "//span[@class='fullListingYears']/h4/text()",
             }
    last_date = '2016-08-31'

    def __init__(self, callback,ldate='2016-08-31', *args, **kwargs):
        super(NVDCVEUpdateClass, self).__init__(*args, **kwargs)
        self.last_date = ldate
        self.callback = callback

    def parse(self, response):
        item = CVEItem()


        #******************** Update date ****************
        last_update_date = datetime.strptime(self.last_date, '%Y-%m-%d').date()
        #********************* Year List***************
        year_list = response.xpath(self.xpath['YearList']).extract()

        #year_list = response.xpath("//span[@class='fullListingYears']/h4/text()").extract()

        month_list = []
        monthList = []
        for year in year_list:
            if int(year) >= last_update_date.year:
                monthList = response.xpath("//span[@class='fullListingYears']/h4[.='%s']/following-sibling::table[1]/tr/td/a/text()" %year).extract()
                for item in monthList:
                    if datetime.strptime(str(item), '%B').month >= last_update_date.month:
                        year_month = {}
                        year_month["year"] = year
                        year_month["month"] = datetime.strptime(str(item), '%B').month
                        month_list.append(year_month)

        for month_year_dict in month_list:
            year = month_year_dict["year"]
            month = month_year_dict["month"]
            yield scrapy.Request('https://nvd.nist.gov/full_listing.cfm?year=%s&month=%s' % (year, month), self.parse_cve)

    def parse_cve(self, response):
        Total_CVE = ",".join([s for s in response.xpath(
            "//body/form/div[@id='container']/div[@id='contents']/div/span[@class='fullListingMonth']/p/a/text()").extract()])
        cve_list = Total_CVE.split(",")
        for cve in cve_list:
            yield scrapy.Request('https://web.nvd.nist.gov/view/vuln/detail?vulnId=%s' % cve, self.parse_info)

    def parse_info(self, response):
        item = CVEItem()
        item['callback'] = self.callback
        path1 = "//body/form/div[@id='container']//div[@class ='vuln-detail']"
        item['URL'] = str(response.url)
        item['CVE_ID'] = str(response.xpath("//body/form/@action").extract()).split("=")[1].strip("']")
        item['Published'] = str(
            response.xpath(path1 + "//div[descendant::span[text()='Original release date:']]//text()").extract()[
                2]).strip()
        item['Modified'] = str(
            response.xpath(path1 + "//div[descendant::span[text()='Last revised:']]//text()").extract()[2]).strip()
        item['Source'] = str(
            response.xpath(path1 + "//div[descendant::span[text()='Source:']]//text()").extract()[2]).strip()
        item['Description'] = str(response.xpath(path1 + "//p//text()").extract()[0]).strip()

        CVSS_Severity_V3_List = []
        CVSS_V3_Metrics_List = []
        CVSS_Severity_V2_List = []
        CVSS_V2_Metrics_List = []
        CVSS_Severity_V3 = {}
        CVSS_V3_Metrics = {}
        CVSS_Severity_V2 = {}
        CVSS_V2_Metrics = {}
        if response.xpath(path1 + "//div[@class='cvss-row']").extract():
            path2 = path1 + "//div[@class='cvss-row']//div[@class='cvss-detail']"
            CVSS_Score_Xpath = response.xpath(path2 + "//h5//text()").extract()
            for cvss in CVSS_Score_Xpath:
                if response.xpath(
                                path1 + "//div[@class='cvss-row']//div[@id = 'BodyPlaceHolder_cplPageContent_plcZones_lt_zoneCenter_VulnerabilityDetail_VulnFormView_Vuln3CvssPanel']"):
                    if str(cvss).__eq__("CVSS Severity (version 3.0):"):
                        CVSS_Severity_V3["CVSS_v3_Base_Score"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='CVSS v3 Base Score:']]//text()").extract()[
                                                                         3]) + " " + str(response.xpath(
                            path2 + "//div[descendant::span[text()='CVSS v3 Base Score:']]//text()").extract()[
                                                                                             4]).strip()
                        CVSS_Severity_V3["Vector"] = str(
                            response.xpath(path2 + "//div[descendant::span[text()='Vector:']]//a//text()").extract()[0])
                        CVSS_Severity_V3["Impact_Score"] = str(
                            response.xpath(path2 + "//div[descendant::span[text()='Impact Score:']]//text()").extract()[
                                2]).strip()
                        CVSS_Severity_V3["Exploitability_Score"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Exploitability Score:']]//text()").extract()[
                                                                           2]).strip()
                    elif str(cvss).__eq__("CVSS Version 3 Metrics:"):
                        CVSS_V3_Metrics["Attack_Vector"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Attack Vector (AV):']]//text()").extract()[
                                                                   2]).strip()
                        CVSS_V3_Metrics["Attack_Complexity"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Attack Complexity (AC):']]//text()").extract()[
                                                                       2]).strip()
                        CVSS_V3_Metrics["Privileges_Required"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Privileges Required (PR):']]//text()").extract()[
                                                                         2]).strip()
                        CVSS_V3_Metrics["User_Interaction"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='User Interaction (UI):']]//text()").extract()[
                                                                      2]).strip()
                        CVSS_V3_Metrics["Scope"] = str(
                            response.xpath(path2 + "//div[descendant::span[text()='Scope (S):']]//text()").extract()[
                                2]).strip()
                        CVSS_V3_Metrics["Confidentiality"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Confidentiality (C):']]//text()").extract()[
                                                                     2]).strip()
                        CVSS_V3_Metrics["Integrity"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Integrity (I):']]//text()").extract()[2]).strip()
                        CVSS_V3_Metrics["Availability"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Availability (A):']]//text()").extract()[2]).strip()
                elif response.xpath(
                                path1 + "//div[@class='cvss-row']//div[@id = 'BodyPlaceHolder_cplPageContent_plcZones_lt_zoneCenter_VulnerabilityDetail_VulnFormView_Vuln2CvssPanel']"):
                    if str(cvss).__eq__("CVSS Severity (version 2.0):"):
                        CVSS_Severity_V2["CVSS_v2_Base_Score"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='CVSS v2 Base Score:']]//text()").extract()[
                                                                         3]) + " " + str(response.xpath(
                            path2 + "//div[descendant::span[text()='CVSS v2 Base Score:']]//text()").extract()[
                                                                                             4]).strip()
                        CVSS_Severity_V2["Vector"] = str(
                            response.xpath(path2 + "//div[descendant::span[text()='Vector:']]//a//text()").extract()[0])
                        CVSS_Severity_V2["Impact_Subscore"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Impact Subscore:']]//text()").extract()[2]).strip()
                        CVSS_Severity_V2["Exploitability_Subscore"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Exploitability Subscore:']]//text()").extract()[
                                                                              2]).strip()
                    elif str(cvss).__eq__("CVSS Version 2 Metrics:"):
                        CVSS_V2_Metrics["Access_Vector"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Access Vector:']]//text()").extract()[2]).strip()
                        CVSS_V2_Metrics["Access_Complexity"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Access Complexity:']]//text()").extract()[
                                                                       2]).strip()
                        CVSS_V2_Metrics["Authentication"] = str(response.xpath(
                            path2 + "//div[descendant::span[text()='Authentication:']]//text()").extract()[2]).strip()
                        CVSS_V2_Metrics["Impact_Type"] = str(
                            response.xpath(path2 + "//div[descendant::span[text()='Impact Type:']]//text()").extract()[
                                2]).strip()

        CVSS_Severity_V3_List.append(dict((k, v) for k, v in CVSS_Severity_V3.iteritems() if v)) if dict(
            (k, v) for k, v in CVSS_Severity_V3.iteritems() if v) != {} else None
        CVSS_V3_Metrics_List.append(dict((k, v) for k, v in CVSS_V3_Metrics.iteritems() if v)) if dict(
            (k, v) for k, v in CVSS_V3_Metrics.iteritems() if v) != {} else None
        CVSS_Severity_V2_List.append(dict((k, v) for k, v in CVSS_Severity_V2.iteritems() if v)) if dict(
            (k, v) for k, v in CVSS_Severity_V2.iteritems() if v) != {} else None
        CVSS_V2_Metrics_List.append(dict((k, v) for k, v in CVSS_V2_Metrics.iteritems() if v)) if dict(
            (k, v) for k, v in CVSS_V2_Metrics.iteritems() if v) != {} else None

        item['CVSS_Severity_version3'] = ""
        item['CVSS_Severity_version2'] = ""
        item['CVSS_Version3_Metrics'] = ""
        item['CVSS_Version2_Metrics'] = ""

        if len(CVSS_Severity_V3_List) != 0:
            item['CVSS_Severity_version3'] = ",".join([str(i) for i in CVSS_Severity_V3_List])
        if len(CVSS_Severity_V2_List) != 0:
            item['CVSS_Severity_version2'] = ",".join([str(i) for i in CVSS_Severity_V2_List])
        if len(CVSS_V3_Metrics_List) != 0:
            item['CVSS_Version3_Metrics'] = ",".join([str(i) for i in CVSS_V3_Metrics_List])
        if len(CVSS_V2_Metrics_List) != 0:
            item['CVSS_Version2_Metrics'] = ",".join([str(i) for i in CVSS_V2_Metrics_List])

        # item['Referencesto_Advisories_Solutions_Tools'] = str(response.xpath(path1 + "//div[descendant::h4[text()='References to Advisories, Solutions, and Tools']]//p//text()").extract()).replace("\\r\\n", "").replace("                ", "")

        if response.xpath(path1 + "//div[@class='entry']").extract():
            external_sources = []
            external_source = {}
            for value in range(1, len(response.xpath(path1 + "//div[@class='entry']").extract()) + 1):
                for index in range(0, len(
                        response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract())):
                    if response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                        index] == "Name:":
                        external_source["Reference_Name"] = str(
                            response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                                index + 1]).replace("  ", "")
                    if response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                        index] == "External Source:":
                        external_source['Reference_Eternal_Source'] = str(
                            response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                                index + 1]).replace("  ", "")
                    if response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                        index] == "US-CERT Vulnerability Note:":
                        external_source['References_US_CERT_Vulnerability_Note'] = str(
                            response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                                index + 1]).replace("  ", "")
                    if response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                        index] == "Type:":
                        external_source['References_Type'] = str(
                            response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                                index + 1]).replace("  ", "")
                    if response.xpath(path1 + "//div[@class='entry'][%s]//text()" % (value)).extract()[
                        index] == "Hyperlink:":
                        external_source['References_link'] = str(
                            response.xpath(path1 + "//div[@class='entry'][%s]//a//text()" % (value)).extract()).replace(
                            "  ", "")
                external_sources.append((str(dict((k, v) for k, v in external_source.iteritems() if v)))) if dict(
                    (k, v) for k, v in external_source.iteritems() if v) != {} else None
                external_source = {}

        item['References'] = ",".join(external_sources)

        ConfText = response.xpath("//body/form/div[@id='container']//div[@class ='vuln-detail']//div[@class='configurations']//span//text()").extract()
        staff = ["AND", "OR", "cpe"]
        ConfText_List = []
        for Confitem in ConfText:
            for staffitem in staff:
                if Confitem:
                    if re.search(staffitem, Confitem):
                        ConfText_List.append(Confitem)
        cpe = "{"
        temp = 1
        for conf_item in ConfText_List:
            if (conf_item in [" AND", " OR"]):
                if temp:
                    cpe += (conf_item + "{")
                    temp = 1
                else:
                    cpe += "}," + (conf_item + "{")
                    temp = 1
            else:
                if temp:
                    cpe += (conf_item)
                    temp = 0
                else:
                    cpe += ("," + conf_item)
                    temp = 0
        cpe += "}}"
        if cpe != "{}}":
            print cpe
            item["Vulnerable"] = str(cpe)


        item["Technical_Details"] = ",".join([s for s in response.xpath(path1 + "//div[@class='technicalDetails']//ul//li//a//text()").extract()])

        yield item
