import os
from scrapy.spiders import XMLFeedSpider
from attackKB_crawler.items.cve_items import CVEItems
from datetime import datetime

class CVEMitreSpider(XMLFeedSpider):

        name = 'CVE_Mitre'
        allowed_domains = ['https://cve.mitre.org']
        namespaces = [
            ("vuln", "http://www.icasi.org/CVRF/schema/vuln/1.1")
        ]
        filepath = "file:///" + os.path.abspath("allitems-cvrf.xml")
        start_urls = [filepath]
        itertag = 'vuln:Vulnerability'
        iterator = 'xml'
        custom_settings = {
            'ITEM_PIPELINES': {
                'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
                #'attackKB_crawler.pipelines.cve_mitre_pipelines.CVEMitreMySQLStorePipeline': 300,
                #'attackKB_crawler.pipelines.cve_mitre_pipelines.CVEMitreJsonWriterPipeline': 800,
            },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CVEMitreSpider, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CVE mitre item")
            item = CVEItems()
            item['callback'] = self.callback
            CVE_ID = ",".join([s for s in node.xpath('vuln:CVE/text()').extract()])
            item['CVE_ID'] = CVE_ID
            item['URL'] = "http://cve.mitre.org/cgi-bin/cvename.cgi?name=%s" % str(CVE_ID).split("CVE-")[1]
            publish_str = "".join([s for s in node.xpath('vuln:Notes/vuln:Note[@Title="Published"]/text()').extract()])
            modify_str = "".join([s for s in node.xpath('vuln:Notes/vuln:Note[@Title="Modified"]/text()').extract()])
            item['Published'] = publish_str #datetime.strptime(publish_str, '%Y-%m-%d')
            item['Modified'] = modify_str #datetime.strptime(modify_str, '%Y-%m-%d')
            references_list =[]
            for reference in node.xpath('vuln:References/vuln:Reference'):
                ref_dict = {}
                ref_dict["Reference_Name"] = reference.xpath("vuln:URL/text()")
                ref_dict["References_link"] = reference.xpath("vuln:Description/text()")
                references_list.append(dict((k, v) for k, v in ref_dict.iteritems() if v)) if dict((k, v) for k, v in ref_dict.iteritems() if v) != {} else None
            item['References'] = ",".join([str(i) for i in references_list])
            desc = ",".join([s for s in node.xpath('vuln:Notes/vuln:Note[@Type="Description"]/text()').extract()])
            item['Description'] = desc
            item['Status']=""
            if len(desc)>10:
                if "*" in desc[0:10] :
                    array_desc = desc.split("*")
                    if len(array_desc) > 2:
                        item['Status'] = array_desc[2]

            '''
            #uncomment if MySQl pipline needed!
            item["Bugtraq_ID"] =""
            item["Source"] =""
            item["Class"] =""
            item["CVSS_Severity_version3"] =""
            item["CVSS_Severity_version2"] =""
            item["CVSS_Version3_Metrics"] =""
            item["CVSS_Version2_Metrics"] =""
            item["Vulnerable"] =""
            item["Not_Vulnerable"] =""
            item["Exploit"] =""
            item["Exploit_file"] =""
            item["Solution"] =""
            item["Patch_file"] =""
            item["Remote"] =""
            item["Local"] =""
            item["Credit"] =""
            item["Technical_Details"] =""
            '''
            yield item