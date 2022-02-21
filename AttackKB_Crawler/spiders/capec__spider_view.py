import os
from scrapy.spiders import XMLFeedSpider
from attackKB_crawler.items.capec_items import CapecMitreViewItems
from attackKB_crawler.util.CustomFunctions import *
import platform


class CapecMitreSpider_View(XMLFeedSpider):

        name = 'CAPEC_View'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]
        itertag = 'capec:View'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            #'attackKB_crawler.pipelines.capec_pipelines.CapecMitreViewMySQLStorePipeline': 932,
            #'attackKB_crawler.pipelines.capec_pipelines.CAPECViewJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_View, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CAPEC View Node")


            item = CapecMitreViewItems()
            item['callback'] = self.callback
            item['Capec_Type'] = "View"
            item['View_Structure'] = ",".join([s for s in node.xpath('capec:View_Structure/text()').extract()])
            item['View_Objective'] = ",".join([str(i) for i in structured_text_type(self,node.xpath('capec:View_Objective'))])
            item['Capec_ID'] = ",".join([s for s in node.xpath('@ID').extract()])
            item['Capec_Name'] = ",".join([s for s in node.xpath('@Name').extract()])
            item['Capec_status'] = ",".join([s for s in node.xpath('@Status').extract()])
            item['View_Filter'] = ",".join([s for s in node.xpath('capec:View_Filter/text()').extract()])

            View_Audience_List = []
            for View_Audience in node.xpath('capec:View_Audience/capec:Audience'):
                View_Audience_tmp = {}
                View_Audience_tmp["Stakeholder"] = ",".join([s for s in View_Audience.xpath('capec:Stakeholder/text()').extract()])
                View_Audience_tmp["Stakeholder_Description"] =  ",".join([str(i) for i in structured_text_type(self,View_Audience.xpath('capec:Stakeholder_Description'))])
                View_Audience_List.append(dict((k, v) for k, v in View_Audience_tmp.iteritems() if v)) if dict((k, v) for k, v in View_Audience_tmp.iteritems() if v ) != {} else None

            item['View_Audience'] = ",".join([str(i) for i in View_Audience_List])

            item['Relationships'] = ",".join([str(i) for i in relationshiptype(self,node.xpath('capec:Relationships/capec:Relationship'))])

            item['Relationship_Notes'] = ",".join([str(i) for i in structured_text_type(self,node.xpath('capec:Relationship_Notes/capec:Relationship_Note'))])

            item['Maintenance_Notes'] = ",".join([str(i) for i in structured_text_type(self,node.xpath('capec:Maintenance_Notes/capec:Maintenance_Note'))])

            item['Other_Notes'] = ",".join([str(i) for i in structured_text_type(self,node.xpath('capec:Other_Notes/capec:Note'))])

            Alternate_Terms_list=[]
            for Alternate_Term_node in node.xpath('capec:Alternate_Terms/capec:Alternate_Term'):
                Alternate_Terms_tmp ={}
                Alternate_Terms_tmp['Term'] = ",".join([s for s in Alternate_Term_node.xpath('capec:Term/text()').extract()])
                Alternate_Terms_tmp['Alternate_Term_Description'] = ",".join([str(i) for i in structured_text_type(self,Alternate_Term_node.xpath('capec:Alternate_Term_Description'))])
                Alternate_Terms_list.append(dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v)) if dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v ) != {} else None

            item['Alternate_Terms'] = ",".join([str(i) for i in Alternate_Terms_list])

            item['Research_Gaps'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Research_Gaps/capec:Research_Gap'))])

            item['References'] = ",".join( [str(i) for i in reference(self , node.xpath('capec:References/capec:Reference'))])

            item['Content_History'] = ",".join([str(i) for i in content_history(self,node.xpath('capec:Content_History'))])

            yield item

