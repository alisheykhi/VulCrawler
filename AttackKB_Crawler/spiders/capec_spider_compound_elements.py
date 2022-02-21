import scrapy
from scrapy.spiders import XMLFeedSpider
import os,platform
from attackKB_crawler.items.capec_items import CapecMitreCompoundElementsItems
from attackKB_crawler.util.CustomFunctions import *


class CapecMitreSpider_CompoundElements(XMLFeedSpider):

        name = 'CAPEC_CompoundElements'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]
        itertag = 'capec:Compound_Element'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECPostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CapecMitreCompoundElementsMySQLStorePipeline': 932,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECCompoundElementsJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_CompoundElements, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CAPEC Compound_Elements Node")
            item = CapecMitreCompoundElementsItems()
            item['callback'] = self.callback
            item['Capec_Type'] = "Compound_Element"

            Description_list = []
            for Description_node in node.xpath('capec:Description'):
                Description_tmp = {}
                Description_tmp['Description_Summary'] = ",".join([s for s in Description_node.xpath('capec:Description_Summary/text()').extract()])
                Description_tmp['Extended_Description'] = ",".join([str(i) for i in structured_text_type(self,Description_node.xpath('capec:Extended_Description'))])
                Description_list.append(dict((k, v) for k, v in Description_tmp.iteritems() if v)) if dict((k, v) for k, v in Description_tmp.iteritems() if v ) != {} else None

            item['Description'] = ",".join([str(i) for i in Description_list])

            item['Relationships'] = ",".join([str(i) for i in relationshiptype(self, node.xpath('capec:Relationships/capec:Relationship'))])

            item['Relationship_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Relationship_Notes/capec:Relationship_Note'))])

            item['Maintenance_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Maintenance_Notes/capec:Maintenance_Note'))])

            item['Background_Details'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Background_Details/capec:Background_Detail'))])

            item['Other_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Other_Notes/capec:Note'))])

            Alternate_Terms_list = []
            for Alternate_Term_node in node.xpath('capec:Alternate_Terms/capec:Alternate_Term'):
                Alternate_Terms_tmp = {}
                Alternate_Terms_tmp['Term'] = ",".join([s for s in Alternate_Term_node.xpath('capec:Term/text()').extract()])
                Alternate_Terms_tmp['Alternate_Term_Description'] = ",".join([str(i) for i in structured_text_type(self,Alternate_Term_node.xpath('capec:Alternate_Term_Description'))])
                Alternate_Terms_list.append(dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v)) if dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v ) != {} else None

            item['Alternate_Terms'] = ",".join([str(i) for i in Alternate_Terms_list])

            item['Research_Gaps'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Research_Gaps/capec:Research_Gap'))])

            item['References'] = ",".join([str(i) for i in reference(self,node.xpath('capec:References/capec:Reference'))])

            item['Content_History'] = ",".join([str(i) for i in content_history(self,node.xpath('capec:Content_History'))])

            item['ID'] = ",".join([s for s in node.xpath('@ID').extract()])

            item['Name'] = ",".join([s for s in node.xpath('@Name').extract()])

            item['Compound_Element_Abstraction'] = ",".join([s for s in node.xpath('@Compound_Element_Abstraction').extract()])

            item['Compound_Element_Completeness'] = ",".join([s for s in node.xpath('@Compound_Element_Completeness').extract()])

            item['Compound_Element_Structure'] = ",".join([s for s in node.xpath('@Compound_Element_Structure').extract()])

            item['Status'] = ",".join([s for s in node.xpath('@ID').extract('@Status')])

            yield item