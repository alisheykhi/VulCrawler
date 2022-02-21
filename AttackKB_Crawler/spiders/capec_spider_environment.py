import scrapy
from scrapy.spiders import XMLFeedSpider
import os,platform
from attackKB_crawler.items.capec_items import CapecMitreEnvironmentItems
from attackKB_crawler.util.CustomFunctions import *


class CapecMitreSpider_Environment(XMLFeedSpider):

        name = 'CAPEC_Environment'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]

        itertag = 'capec:Environment'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            #'attackKB_crawler.pipelines.capec_pipelines.CAPECPostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CapecMitreEnvironmentMySQLStorePipeline': 932,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECEnvironmentJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_Environment, self).__init__(*args, **kwargs)
            self.callback = callback


        def parse_node(self, response, node):
            self.logger.info("CAPEC Environment Node")
            item = CapecMitreEnvironmentItems()
            item['callback'] = self.callback
            item['Capec_Type'] = "Environment"
            item['Environment_ID'] = ",".join([s for s in node.xpath('@ID').extract()])
            item['Environment_Title'] = ",".join([s for s in node.xpath('capec:Environment_Title/text()').extract()])
            item['Environment_Description'] = ",".join([s for s in node.xpath('capec:Environment_Description/text()').extract()])
            yield item