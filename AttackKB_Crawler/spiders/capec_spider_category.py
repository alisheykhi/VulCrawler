import scrapy
from scrapy.spiders import XMLFeedSpider
import os,platform
from attackKB_crawler.items.capec_items import CapecMitreCategoryItems
from attackKB_crawler.util.CustomFunctions import *


class CapecMitreSpider_Category(XMLFeedSpider):

        name = 'CAPEC_Category'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]
        itertag = 'capec:Category'
        iterator = 'xml'
        custom_settings = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECPostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CapecMitreCategoryMySQLStorePipeline': 932,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECCategoryJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_Category, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CAPEC Category Node")
            item = CapecMitreCategoryItems()
            item['callback'] = self.callback

            item['Capec_Type'] = "Category"

            item['Capec_ID'] = ",".join([s for s in node.xpath('@ID').extract()])

            item['Capec_Name'] = ",".join([s for s in node.xpath('@Name').extract()])

            item['Capec_status'] = ",".join([s for s in node.xpath('@Status').extract()])

            Description_list = []
            for Description_node in node.xpath('capec:Description'):
                Description_tmp = {}
                Description_tmp['Description_Summary'] = ",".join([s for s in Description_node.xpath('capec:Description_Summary/text()').extract()])
                Description_tmp['Extended_Description'] = ",".join([str(i) for i in structured_text_type(self, Description_node.xpath('capec:Extended_Description'))])
                Description_list.append(dict((k, v) for k, v in Description_tmp.iteritems() if v)) if dict((k, v) for k, v in Description_tmp.iteritems() if v ) != {} else None

            item['Description'] = ",".join([str(i) for i in Description_list])

            item['Related_Weakness'] = ",".join([str(i) for i in related_weakness(self, node.xpath('capec:Related_Weaknesses/capec:Related_Weakness'))])

            item['Attack_Prerequisite'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Attack_Prerequisites/capec:Attack_Prerequisite'))])

            item['Methods_of_Attack'] = ",".join([s for s in node.xpath('capec:Methods_of_Attack/capec:Method_of_Attack/text()').extract()])

            item['Attacker_Skills_or_Knowledge_Required'] = ",".join([str(i) for i in attacker_skills_or_knowledge_required(self, node.xpath('capec:Attacker_Skills_or_Knowledge_Required/capec:Attacker_Skill_or_Knowledge_Required'))])

            item['Resources_Required'] = ",".join([str(i) for i in structured_text_type(self,node.xpath('capec:Resources_Required'))])

            item['Attack_Motivation_Consequences'] = ",".join([str(i) for i in attack_motivation_consequence(self , node.xpath('capec:Attack_Motivation-Consequences/capec:Attack_Motivation-Consequence'))])

            item['Relationships'] = ",".join([str(i) for i in relationshiptype(self, node.xpath('capec:Relationships/capec:Relationship'))])

            item['Relationship_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Relationship_Notes/capec:Relationship_Note'))])

            item['Maintenance_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Maintenance_Notes/capec:Maintenance_Note'))])

            item['Background_Details'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Background_Details/capec:Background_Detail'))])

            item['Other_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Other_Notes/capec:Note'))])

            Alternate_Terms_list = []
            for Alternate_Term_node in node.xpath('capec:Alternate_Terms/capec:Alternate_Term'):
                Alternate_Terms_tmp = {}
                Alternate_Terms_tmp['Term'] = ",".join([s for s in Alternate_Term_node.xpath('capec:Term/text()').extract()])
                Alternate_Terms_tmp['Alternate_Term_Description'] = ",".join([str(i) for i in structured_text_type(Alternate_Term_node.xpath('capec:Alternate_Term_Description'))])
                Alternate_Terms_list.append(dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v)) if dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v ) != {} else None

            item['Alternate_Terms'] = ",".join([str(i) for i in Alternate_Terms_list])

            item['Research_Gaps'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Research_Gaps/capec:Research_Gap'))])

            item['References'] = ",".join([str(i) for i in reference(self,node.xpath('capec:References/capec:Reference'))])

            item['Content_History'] = ",".join([str(i) for i in content_history(self,node.xpath('capec:Content_History'))])
            yield item
