import os,platform

from scrapy.spiders import XMLFeedSpider

from attackKB_crawler.items.cwe_mitre_items import CWEMitreViewItems
from attackKB_crawler.util.cwe_common_attribute import *


class CweMitreViewSpider(XMLFeedSpider):

        name = 'CWE_Views'
        allowed_domains = ['http://cwe.mitre.org/']
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("cwe.xml")
        start_urls = [filepath]
        itertag = 'View'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            #'attackKB_crawler.pipelines.cwe_mitre_pipelines.CWEMitreViewMySQLStorePipeline': 932,
            #'attackKB_crawler.pipelines.cwe_mitre_pipelines.CWEViewJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CweMitreViewSpider, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CWE View Node")
            item = CWEMitreViewItems()
            item['callback'] = self.callback
            item['CWE_Type'] = "View"
            item['View_Structure'] = ",".join([s for s in node.xpath('View_Structure/text()').extract()])
            item['View_Objective'] = "".join([s for s in node.xpath('View_Objective/Text/text()').extract()])
            item['CWE_ID'] = "".join([s for s in node.xpath('@ID').extract()])
            item['CWE_Name'] = ",".join([s for s in node.xpath('@Name').extract()])
            item['CWE_status'] = ",".join([s for s in node.xpath('@Status').extract()])

            View_Audience = []
            for audience in node.xpath('View_Audience/Audience'):
                Audience = {}
                Audience["Stakeholder"] = "".join(audience.xpath('Stakeholder/text()').extract())
                Audience["Stakeholder_Description"] = "".join(audience.xpath('Stakeholder_Description/Text/text()').extract())
                View_Audience.append(dict((k, v) for k, v in Audience.iteritems() if v))if dict((k, v) for k, v in Audience.iteritems() if v ) != {} else None
            item['View_Audience'] = ",".join(str(s) for s in View_Audience)

            View_Filter = "".join(node.xpath('View_Filter/text()').extract())
            item['View_Filter'] = View_Filter

            # ************************************* Common_Attributes **********************************
            item['Relationships'] = ",".join([str(i) for i in Relationships(self, node.xpath('Relationships'))])
            item['Relationship_Notes'] = ",".join([str(i) for i in Relationship_Notes(self, node.xpath('Relationship_Notes'))])
            item['Maintenance_Notes'] = ",".join([str(i) for i in Maintenance_Notes(self, node.xpath('Maintenance_Notes'))])
            item['Other_Notes'] = ",".join([str(i) for i in Other_Notes(self, node.xpath('Other_Notes'))])
            item['Alternate_Terms'] = ",".join([str(i) for i in Alternate_Terms(self, node.xpath('Alternate_Terms'))])
            item['Research_Gaps'] = ",".join([str(i) for i in Research_Gaps(self, node.xpath('Research_Gaps'))])
            item['References'] = ",".join([str(i) for i in References(self, node.xpath('References'))])
            item['Content_History'] = ",".join([str(i) for i in Content_History(self , node.xpath('Content_History'))])

            yield item









