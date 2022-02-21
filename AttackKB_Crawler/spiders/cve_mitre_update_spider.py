from attackKB_crawler.items.cve_items import CVEItems
import scrapy
from datetime import datetime
import re


class CVEMitreUpdateClass(scrapy.Spider):

    name = 'Update_CVE_Mitre'
    allowed_domains = ['https://cve.mitre.org/']
    #start_urls = ['https://cassandra.cerias.purdue.edu/CVE_changes/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            #'attackKB_crawler.pipelines.securityfocus_pipelines.SecurityFocusMySQLStorePipeline': 932,
            #'attackKB_crawler.pipelines.securityfocus_pipelines.SecurityFocusJsonWriterPipeline': 900,
        },
    }
    last_date = datetime.strptime('2016-07-31', '%Y-%m-%d')
    xpath = {
        "1": "//hr[1]/preceding-sibling::node()[count(.| //hr[1]/preceding-sibling::node()) = count(//hr[1]/preceding-sibling::node())]",
        "other": "//hr[1]/following-sibling::node()[count(.| //hr[1]/preceding-sibling::node()) = count(//hr[1]/preceding-sibling::node())]",
        "last": "//hr[22]/following-sibling::node()[count(.| //hr[22]/following-sibling::node()) = count(//hr[22]/following-sibling::node())]"
        }

    def __init__(self,callback, ldate='2016-07-31', *args, **kwargs):
        super(CVEMitreUpdateClass, self).__init__(*args, **kwargs)
        self.last_date = datetime.strptime(ldate, '%Y-%m-%d')
        self.callback = callback

    def start_requests(self):
        yield scrapy.Request('https://cassandra.cerias.purdue.edu/CVE_changes/' , self.extract_link_from_update_page)

    def extract_link_from_update_page(self, response):
        url_list =[]
        tr_xpath = response.xpath("//body//tr")
        tr_count = len(tr_xpath)
        for index_tr in range(4, tr_count):
            first_part = "https://cassandra.cerias.purdue.edu/CVE_changes/"
            second_part = str(response.xpath("//body//tr[%s]/td[%s]/a/@href" % (index_tr, 2)).extract()[0])
            Reference = first_part + second_part

            date_string = str(response.xpath("//body//tr[%s]/td[%s]/text()" % (index_tr, 3)).extract()[0]).strip()
            Date_Time = datetime.strptime(date_string , '%d-%b-%Y %H:%M')

            if Date_Time > self.last_date and "CVE" in second_part:
                second_part2 = second_part.replace("CVE." , "")
                if re.match('^\d{4}.\d{2}.html', second_part2) is not None:
                    url_list.append(Reference)
        for url in url_list:
            yield scrapy.Request(url , callback=self.extract_urls_from_each_link_page , dont_filter=True)

    def extract_urls_from_each_link_page(self, response):
        self.logger.info("casandra item")
        hr = []
        hr.append(response.xpath(self.xpath['1']).extract())
        hr_len = len(response.xpath("//hr"))
        for i in range(1, hr_len):
            hr.append(response.xpath(
                "//hr[%s]/following-sibling::node()[count(.| //hr[%s]/preceding-sibling::node()) = count(//hr[%s]/preceding-sibling::node())]" % (i, i + 1, i + 1)).extract())
        hr.append(response.xpath("//hr[%s]/following-sibling::node()" % hr_len).extract())
        new_entries_list=[]
        graduations_list=[]
        modified_list=[]
        for tags in hr:
            find_index = lambda x: [i for i, j in enumerate(tags) if re.match(x, j)][0]
            modified_index = find_index('\nModified entries:')
            graduations_index = find_index('\nGraduations \(CAN to CVE\):')
            new_entries_index = find_index('New entries:')
            extract_link = lambda x, y, z: [re.search(r'<a href="(.*?)">(.+?)</a>', z[i]).groups()[0] for i in range(x, y) if re.match(r'<a.*?>(.+?)</a>', z[i])]

            new_entries = extract_link(new_entries_index, graduations_index, tags)
            graduations = extract_link(graduations_index, modified_index, tags)
            modified = extract_link(modified_index, len(tags), tags)

            date_str = re.search('date: (\d{4}-\d{2}-\d{2})', tags[1]).groups()[0]
            date =datetime.strptime(date_str, '%Y-%m-%d')

            if date > self.last_date:
                new_entries_list.extend(new_entries)
                graduations_list.extend(graduations)
                modified_list.extend(modified)
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        # print "_______________date_________________"
        # print date
        # print "_______________new_entries_list_________________"
        # print new_entries_list
        # print "_______________graduations_list_________________"
        # print graduations_list
        # print "_______________modified_list_________________"
        # print modified_list
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

        for url in new_entries_list:
            yield scrapy.Request(url, callback=self.parse_cve_content, dont_filter=True)
        for url in graduations_list:
            yield scrapy.Request(url, callback=self.parse_cve_content, dont_filter=True)
        for url in modified_list:
            yield scrapy.Request(url, callback=self.parse_cve_content, dont_filter=True)

    def parse_cve_content(self, response):
        item = CVEItems()
        item['callback'] = self.callback

        tr_count = len(response.xpath("//body//div[@id = 'GeneratedTable']//tr"))
        for i in range (0,tr_count):
            if i == 2:
                CVE_ID = response.xpath("//body//div[@id = 'GeneratedTable']//tr[%s]/td/h2/text()" %i).extract()[0].strip()
            elif i == 4:
                Description = response.xpath("//body//div[@id = 'GeneratedTable']//tr[%s]/td/text()" % i).extract()[0].strip()

            elif i == 7:
                li_List = []
                li_count = len(response.xpath("//body//div[@id = 'GeneratedTable']//tr[%s]/td/ul/li" %i))
                for j in range(1, li_count+1):
                    li_List.append(response.xpath("//body//div[@id = 'GeneratedTable']//tr[%s]/td/ul/li[%s]//text()" %(i , j)).extract()[0].strip())

                index=0
                list_ref_desc =[]
                while (index< len(li_List)):

                    Data_index = str(li_List[index]).split(":")[0]
                    if index+1 < len(li_List):
                        Data_index_1 = str(li_List[index+1]).split(":")[0]
                    else:
                        Data_index_1 = ""
                    if Data_index_1 == "URL" and Data_index != "URL":
                        dict_ref_desc = {}
                        dict_ref_desc["Reference_Name"] = li_List[index]
                        dict_ref_desc["References_link"] =  li_List[index+1]
                        list_ref_desc.append(dict((k, v) for k, v in dict_ref_desc.iteritems() if v)) if dict((k, v) for k, v in dict_ref_desc.iteritems() if v) != {} else None
                        index += 2
                    else:
                        dict_ref_desc = {}
                        dict_ref_desc["Reference_Name"] = li_List[index]
                        dict_ref_desc["References_link"] = li_List[index].split(":")[1]+li_List[index].split(":")[2]
                        list_ref_desc.append(dict((k, v) for k, v in dict_ref_desc.iteritems() if v)) if dict((k, v) for k, v in dict_ref_desc.iteritems() if v) != {} else None
                        index +=1

                Reference = list_ref_desc

            elif i == 9:
                Published_str = "".join(response.xpath("//body//div[@id = 'GeneratedTable']//tr[%s]/td/b/text()" %i).extract())
                Published = datetime.strptime(Published_str, '%Y%m%d')

            elif i == 11:
                modify_str = re.search(r'.*\((\d{8})\)',",".join(response.xpath("//body//div[@id = 'GeneratedTable']//tr[%s]/td/text()" % i ).extract())).groups()[0]
                Modified = datetime.strptime(modify_str, '%Y%m%d')

        if len(Description) > 10:
            if "*" in Description[0:10]:
                array_desc = Description.split("*")
                if len(array_desc) > 2:
                    item['Status'] = array_desc[2]

        item['CVE_ID'] = CVE_ID
        item['Description'] = Description
        item['Published'] = Published_str
        item['Modified'] = modify_str
        item['References'] = Reference

        yield item