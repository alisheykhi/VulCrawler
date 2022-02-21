import logging
import scrapy
from scrapy.spiders import XMLFeedSpider
import os,platform

from attackKB_crawler.items.capec_items import CapecMitreAttackPatternItems
from attackKB_crawler.util.CustomFunctions import *

class CapecMitreSpider_AttackPattern(XMLFeedSpider):
#capec_AttackPattern
        name = 'CAPEC_AttackPattern'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath + os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]
        itertag = 'capec:Attack_Pattern'
        iterator = 'xml'
        custom_settings = {
         'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipline.PostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECPostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CapecMitreAttackPatternMySQLStorePipeline': 932,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECAttackPatternJsonWriterPipeline': 900,
        },
         }


        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_AttackPattern, self).__init__(*args, **kwargs)
            self.callback = callback


        def parse_node(self, response, node):
            self.logger.info("CAPEC Attack Pattern Node")
            item = CapecMitreAttackPatternItems()
            item['callback'] = self.callback
            item['Capec_Type'] = "AttackPattern"
            item['Capec_ID'] = ",".join([s for s in node.xpath('@ID').extract()])
            item['Capec_Name'] = ",".join([s for s in node.xpath('@Name').extract()])
            item['Capec_status'] = ",".join([s for s in node.xpath('@Status').extract()])
            item['Capec_Pattern_Abstraction'] = ",".join([s for s in node.xpath('@Pattern_Abstraction').extract()])
            item['Capec_Pattern_Completeness'] = ",".join([s for s in node.xpath('@Pattern_Completeness').extract()])

            Description_list = []
            for Description_node in node.xpath('capec:Description'):
                Description_tmp = {}
                Description_tmp['Summary'] = ",".join([str(i) for i in structured_text_type(self, Description_node.xpath('capec:Summary'))])
                Description_tmp['Attack_Execution_Flow'] = ",".join([str(i) for i in attack_execution_flow(self, Description_node.xpath('capec:Attack_Execution_Flow'))])
                Description_list.append(dict((k, v) for k, v in Description_tmp.iteritems() if v)) if dict((k, v) for k, v in Description_tmp.iteritems() if v ) != {} else None

            item['Description'] = ",".join([str(i) for i in Description_list])

            Alternate_Terms_list = []
            for Alternate_Term_node in node.xpath('capec:Alternate_Terms/capec:Alternate_Term'):
                Alternate_Terms_tmp = {}
                Alternate_Terms_tmp['Term'] = ",".join([s for s in Alternate_Term_node.xpath('capec:Term/text()').extract()])
                Alternate_Terms_tmp['Alternate_Term_Description'] = ",".join([str(i) for i in structured_text_type(self, Alternate_Term_node.xpath('capec:Alternate_Term_Description'))])
                Alternate_Terms_list.append(dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v)) if dict((k, v) for k, v in Alternate_Terms_tmp.iteritems() if v ) != {} else None

            item['Alternate_Terms'] = ",".join([str(i) for i in Alternate_Terms_list])

            item['Target_Attack_Surface'] = ",".join([str(i) for i in target_attack_surfacetype(self, node.xpath('capec:Target_Attack_Surface'))])

            item['Attack_Prerequisites'] = ",".join([str(i) for i in structured_text_type(self,node.xpath('capec:Attack_Prerequisites/capec:Attack_Prerequisite'))])

            item['Typical_Severity'] = ",".join([s for s in node.xpath('capec:Typical_Severity/text()').extract()])

            Typical_Likelihood_of_Exploit_list = []
            for Typical_Likelihood_of_Exploit_node in node.xpath('capec:Typical_Likelihood_of_Exploit'):
                Typical_Likelihood_of_Exploit_node_tmp = {}
                Typical_Likelihood_of_Exploit_node_tmp["Likelihood"] = ",".join([s for s in Typical_Likelihood_of_Exploit_node.xpath('capec:Likelihood/text()').extract()])
                Typical_Likelihood_of_Exploit_node_tmp["Explanation"] = ",".join([str(i) for i in structured_text_type(self, Typical_Likelihood_of_Exploit_node.xpath('capec:Explanation'))])
                Typical_Likelihood_of_Exploit_list.append(dict((k, v) for k, v in Typical_Likelihood_of_Exploit_node_tmp.iteritems() if v)) if dict((k, v) for k, v in Typical_Likelihood_of_Exploit_node_tmp.iteritems() if v ) != {} else None

            item['Typical_Likelihood_of_Exploit'] = ",".join([str(i) for i in Typical_Likelihood_of_Exploit_list])

            item['Methods_of_Attack'] = ",".join([s for s in node.xpath('capec:Methods_of_Attack/capec:Method_of_Attack/text()').extract()])

            Examples_Instances_list = []
            for Examples_Instance_node in node.xpath('capec:Examples-Instances/capec:Example-Instance'):
                Examples_Instance_tmp ={}
                Examples_Instance_tmp["Description"] = ",".join([str(i) for i in structured_text_type(self, Examples_Instance_node.xpath('capec:Example-Instance_Description'))])
                Examples_Instance_tmp["Example-Instance_Related_Vulnerabilities"] = ",".join([str(i) for i in structured_text_type(self, Examples_Instance_node.xpath('capec:Example-Instance_Related_Vulnerabilities/capec:Example-Instance_Related_Vulnerability'))])
                Examples_Instances_list.append(dict((k, v) for k, v in Examples_Instance_tmp.iteritems() if v)) if dict((k, v) for k, v in Examples_Instance_tmp.iteritems() if v ) != {} else None

            item["Examples_Instances"] = ",".join([str(i) for i in Examples_Instances_list])

            item['Attacker_Skills_or_Knowledge_Required'] = ",".join([str(i) for i in attacker_skills_or_knowledge_required(self,node.xpath('capec:Attacker_Skills_or_Knowledge_Required/capec:Attacker_Skill_or_Knowledge_Required'))])

            item['Resources_Required'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Resources_Required'))])

            Probing_Techniques_List = []
            for Probing_Techniques_node in node.xpath('capec:Probing_Techniques/capec:Probing_Technique'):
                Probing_Techniques_tmp = {}
                Probing_Techniques_tmp["Description"] = ",".join([str(i) for i in structured_text_type(self, Probing_Techniques_node.xpath('capec:Description'))])
                Probing_Techniques_tmp["Observables"] = ",".join([str(i) for i in observablestype(self, Probing_Techniques_node.xpath('capec:Observables'))])
                Probing_Techniques_List.append(dict((k, v) for k, v in Probing_Techniques_tmp.iteritems() if v)) if dict((k, v) for k, v in Probing_Techniques_tmp.iteritems() if v ) != {} else None

            item['Probing_Techniques'] = ",".join([str(i) for i in Probing_Techniques_List])

            Indicators_Warnings_of_Attack_List = []
            for Indicators_Warnings_of_Attack_node in node.xpath('capec:Indicators-Warnings_of_Attack/capec:Indicator-Warning_of_Attack'):
                Indicators_Warnings_of_Attack_tmp = {}
                Indicators_Warnings_of_Attack_tmp["Description"] = ",".join([str(i) for i in structured_text_type(self, Indicators_Warnings_of_Attack_node.xpath('capec:Description'))])
                Indicators_Warnings_of_Attack_tmp["Observables"] = ",".join([str(i) for i in observablestype(self, Indicators_Warnings_of_Attack_node.xpath('capec:Observables'))])
                Indicators_Warnings_of_Attack_List.append(dict((k, v) for k, v in Indicators_Warnings_of_Attack_tmp.iteritems() if v)) if dict((k, v) for k, v in Indicators_Warnings_of_Attack_tmp.iteritems() if v ) != {} else None

            item['Indicators_Warnings_of_Attack'] = ",".join([str(i) for i in Indicators_Warnings_of_Attack_List])

            Obfuscation_Techniques_List = []
            for Obfuscation_Techniques_node in node.xpath('capec:Obfuscation_Techniques/capec:Obfuscation_Technique'):
                Obfuscation_Techniques_tmp = {}
                Obfuscation_Techniques_tmp["Description"] = ",".join([str(i) for i in structured_text_type(self, Obfuscation_Techniques_node.xpath('capec:Description'))])
                Obfuscation_Techniques_tmp["Observables"] = ",".join([str(i) for i in observablestype(self, Obfuscation_Techniques_node.xpath('capec:Observables'))])
                Obfuscation_Techniques_List.append(dict((k, v) for k, v in Obfuscation_Techniques_tmp.iteritems() if v)) if dict((k, v) for k, v in Obfuscation_Techniques_tmp.iteritems() if v ) != {} else None

            item['Obfuscation_Techniques'] = ",".join([str(i) for i in Obfuscation_Techniques_List])

            item['Solutions_and_Mitigations'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Solutions_and_Mitigations/capec:Solution_or_Mitigation'))])

            item['Attack_Motivation_Consequences'] = ",".join([str(i) for i in attack_motivation_consequence(self,node.xpath('capec:Attack_Motivation-Consequences/capec:Attack_Motivation-Consequence'))])

            item['Injection_Vector'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Injection_Vector'))])

            item['Payload'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Payload'))])

            item['Activation_Zone'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Activation_Zone'))])

            Payload_Activation_Impact_list = []
            for Payload_Activation_Impact in node.xpath('capec:Payload_Activation_Impact'):
                Payload_Activation_Impact_tmp = {}
                Payload_Activation_Impact_tmp["Description"] = ",".join([str(i) for i in structured_text_type(self,Payload_Activation_Impact.xpath('capec:Description'))])
                Payload_Activation_Impact_tmp["Observables"] = ",".join([str(i) for i in observablestype(self, Payload_Activation_Impact.xpath('capec:Observables'))])
                Payload_Activation_Impact_list.append(dict((k, v) for k, v in Payload_Activation_Impact_tmp.iteritems() if v)) if dict((k, v) for k, v in Payload_Activation_Impact_tmp.iteritems() if v ) != {} else None

            item['Payload_Activation_Impact'] = ",".join([str(i) for i in Payload_Activation_Impact_list])

            item['Related_Weakness'] = ",".join([str(i) for i in related_weakness(self,node.xpath('capec:Related_Weaknesses/capec:Related_Weakness'))])

            item['Related_Vulnerabilities'] = ",".join([str(i) for i in related_vulnerability(self, node.xpath('capec:Related_Vulnerabilities/capec:Related_Vulnerability'))])

            item['Related_Attack_Patterns'] = ",".join([str(i) for i in relationshiptype(self, node.xpath('capec:Related_Attack_Patterns/capec:Related_Attack_Pattern'))])

            item['Relevant_Security_Requirements'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Relevant_Security_Requirements/capec:Relevant_Security_Requirement'))])

            Relevant_Design_Patterns_list = []
            for Relevant_Design_Patterns_node in node.xpath('capec:Relevant_Design_Patterns'):
                Relevant_Design_Patterns_tmp = {}
                Relevant_Design_Patterns_tmp["Recommended_Design_Patterns"] = ",".join([str(i) for i in structured_text_type(self, Relevant_Design_Patterns_node.xpath('apec:Recommended_Design_Patterns/capec:Recommended_Design_Pattern'))])
                Relevant_Design_Patterns_tmp["Non-Recommended_Design_Pattern"] = ",".join([str(i) for i in structured_text_type(self, Relevant_Design_Patterns_node.xpath('capec:Non-Recommended_Design_Patterns/capec:Non-Recommended_Design_Pattern'))])
                Relevant_Design_Patterns_list.append(dict((k, v) for k, v in Relevant_Design_Patterns_tmp.iteritems() if v)) if dict((k, v) for k, v in Relevant_Design_Patterns_tmp.iteritems() if v ) != {} else None

            item['Relevant_Design_Patterns'] = ",".join([str(i) for i in Relevant_Design_Patterns_list])

            item['Relevant_Security_Patterns'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Relevant_Security_Patterns/capec:Relevant_Security_Pattern'))])

            item['Related_Security_Principles'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Related_Security_Principles/capec:Related_Security_Principle'))])

            item['Related_Guidelines'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Related_Guidelines/capec:Related_Guideline'))])

            item['Purposes'] = ",".join([s for s in node.xpath('capec:Purposes/capec:Purpose/text()').extract()])

            CIA_Impact_list = []
            for CIA_Impact_node in node.xpath('capec:CIA_Impact'):
                CIA_Impact_tmp = {}
                CIA_Impact_tmp["Confidentiality_Impact"] = ",".join([s for s in CIA_Impact_node.xpath('capec:Confidentiality_Impact/text()').extract()])
                CIA_Impact_tmp["Integrity_Impact"] = ",".join([s for s in CIA_Impact_node.xpath('capec:Integrity_Impact/text()').extract()])
                CIA_Impact_tmp["Availability_Impact"] = ",".join([s for s in CIA_Impact_node.xpath('capec:Availability_Impact/text()').extract()])
                CIA_Impact_list.append(dict((k, v) for k, v in CIA_Impact_tmp.iteritems() if v)) if dict((k, v) for k, v in CIA_Impact_tmp.iteritems() if v ) != {} else None

            item['CIA_Impact'] = ",".join([str(i) for i in CIA_Impact_list])

            Technical_Context_list = []
            for Technical_Context_node in node.xpath('capec:Technical_Context'):
                Technical_Context_tmp = {}
                Technical_Context_tmp["Architectural_Paradigm"] = ",".join([s for s in Technical_Context_node.xpath( 'capec:Architectural_Paradigms/capec:Architectural_Paradigm/text()').extract()])
                Technical_Context_tmp["Framework"] = ",".join([s for s in Technical_Context_node.xpath('capec:Frameworks/capec:Framework/text()').extract()])
                Technical_Context_tmp["Platform"] = ",".join([s for s in Technical_Context_node.xpath('capec:Platforms/capec:Platform/text()').extract()])
                Technical_Context_tmp["Language"] = ",".join([s for s in Technical_Context_node.xpath('capec:Languages/capec:Language/text()').extract()])
                Technical_Context_list.append(dict((k, v) for k, v in Technical_Context_tmp.iteritems() if v)) if dict((k, v) for k, v in Technical_Context_tmp.iteritems() if v ) != {} else None

            item['Technical_Context'] = ",".join([str(i) for i in Technical_Context_list])

            item['Keywords'] = ",".join([s for s in node.xpath('capec:Keywords/capec:Keyword/text()').extract()])

            item['References'] = ",".join([str(i) for i in reference(self,node.xpath('capec:References/capec:Reference'))])

            item['Other_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Other_Notes/capec:Note'))])

            item['Maintenance_Notes'] = ",".join([str(i) for i in structured_text_type(self, node.xpath('capec:Maintenance_Notes/capec:Maintenance_Note'))])

            item['Content_History'] = ",".join([str(i) for i in content_history(self,node.xpath('capec:Content_History'))])

            yield item

