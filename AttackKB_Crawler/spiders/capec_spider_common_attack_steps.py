import scrapy
from scrapy.spiders import XMLFeedSpider
import os,platform
from attackKB_crawler.items.capec_items import CapecMitreCommonAttackStepsItems
from attackKB_crawler.util.CustomFunctions import *


class CapecMitreSpider_CommonAttackSteps(XMLFeedSpider):

        name = 'CAPEC_CommonAttackSteps'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]
        itertag = 'capec:Common_Attack_Step'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECPostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CapecMitreCommonAttackStepsMySQLStorePipeline': 932,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECCommonAttackStepsJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_CommonAttackSteps, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CAPEC Common_Attack_Steps Node")
            item = CapecMitreCommonAttackStepsItems()
            item['callback'] = self.callback
            item['Capec_Type'] = "Common_Attack_Step"
            item['Custom_Attack_StepType'] = ",".join([str(i) for i in custom_attack_steptype(self, node)])
            item['Common_Attack_Step_ID'] = ",".join([s for s in node.xpath('@ID').extract()])