import  os,platform

from scrapy.spiders import XMLFeedSpider

from attackKB_crawler.items.cwe_mitre_items import CWEMitreWeaknessItems
from attackKB_crawler.util.cwe_common_attribute import *


class CweMitreWeaknessSpider(XMLFeedSpider):

        name = 'CWE_Weakness'
        allowed_domains = ['http://cwe.mitre.org/']
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("cwe.xml")
        start_urls = [filepath]

        itertag = 'Weakness'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            #'attackKB_crawler.pipelines.cwe_mitre_pipelines.CWEMitreWeaknessMySQLStorePipeline': 932,
            #'attackKB_crawler.pipelines.cwe_mitre_pipelines.CWEWeaknessJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback,  *args, **kwargs):
            super(CweMitreWeaknessSpider, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CWE Weakness Node")
            item = CWEMitreWeaknessItems()
            item['callback'] = self.callback
            item['CWE_Type'] = "Weakness"
            item['CWE_ID'] = "".join([s for s in node.xpath('@ID').extract()])
            item['CWE_Name'] = "".join([s for s in node.xpath('@Name').extract()])
            item['CWE_status'] = "".join([s for s in node.xpath('@Status').extract()])
            item['Weakness_Abstraction'] = "".join([s for s in node.xpath('@Weakness_Abstraction').extract()])

            # ************************************* Common_Attributes **********************************

            item['Description'] = Description(self, node.xpath('Description'))
            item['Relationships'] = Relationships(self, node.xpath('Relationships'))
            item['Relationship_Notes'] = Relationship_Notes(self, node.xpath('Relationship_Notes'))
            item['Weakness_Ordinalities'] = Weakness_Ordinalities(self, node.xpath('Weakness_Ordinalities'))
            item['Applicable_Platforms'] = Applicable_Platforms(self, node.xpath('Applicable_Platforms'))
            item['Maintenance_Notes'] = Maintenance_Notes(self, node.xpath('Maintenance_Notes'))
            item['Background_Details'] = Background_Details(self, node.xpath('Background_Details'))
            item['Other_Notes'] = Other_Notes(self, node.xpath('Other_Notes'))
            item['Alternate_Terms'] = Alternate_Terms(self, node.xpath('Alternate_Terms'))
            item['Terminology_Notes'] = Terminology_Notes(self, node.xpath('Terminology_Notes'))
            item['Time_of_Introduction'] = Time_of_Introduction(self, node.xpath('Time_of_Introduction'))
            item['Modes_of_Introduction'] = Modes_of_Introduction(self, node.xpath('Modes_of_Introduction'))
            item['Enabling_Factors_for_Exploitation'] = Enabling_Factors_for_Exploitation(self, node.xpath('Enabling_Factors_for_Exploitation'))
            item['Likelihood_of_Exploit'] = Likelihood_of_Exploit(self, node.xpath('Likelihood_of_Exploit'))
            item['Common_Consequences'] = Common_Consequences(self, node.xpath('Common_Consequences'))
            item['Detection_Methods'] = Detection_Methods(self, node.xpath('Detection_Methods'))
            item['Potential_Mitigations'] = Potential_Mitigations(self, node.xpath('Potential_Mitigations'))
            item['Causal_Nature'] = Causal_Nature(self, node.xpath('Causal_Nature'))
            item["Demonstrative_Examples"] = Demonstrative_Examples(self, node.xpath('Demonstrative_Examples'))
            item['Observed_Examples'] = Observed_Examples(self, node.xpath('Observed_Examples'))
            item['Theoretical_Notes'] = Theoretical_Notes(self, node.xpath('Theoretical_Notes'))
            item['Functional_Areas'] = Functional_Areas(self, node.xpath('Functional_Areas'))
            item['Relevant_Properties'] = Relevant_Properties(self, node.xpath('Relevant_Properties'))
            item['Affected_Resources'] = Affected_Resources(self, node.xpath('Affected_Resources'))
            item['Research_Gaps'] = Research_Gaps(self, node.xpath('Research_Gaps'))
            item['References'] = References(self, node.xpath('References'))
            item['Taxonomy_Mappings'] = Taxonomy_Mappings(self, node.xpath('Taxonomy_Mappings'))
            item['White_Box_Definitions'] = White_Box_Definitions(self, node.xpath('White_Box_Definitions'))
            item['Black_Box_Definitions'] = Black_Box_Definitions(self, node.xpath('Black_Box_Definitions'))
            item['Related_Attack_Patterns'] = Related_Attack_Patterns(self, node.xpath('Related_Attack_Patterns'))
            item['Content_History'] = Content_History(self, node.xpath('Content_History'))
            return item




