import scrapy
from scrapy.spiders import XMLFeedSpider
import os,platform

from attackKB_crawler.items.capec_items import CapecMitreCommonAttackSurfacesItems
from attackKB_crawler.util.CustomFunctions import *


class CapecMitreSpider_CommonAttackSurfaces(XMLFeedSpider):

        name = 'CAPEC_CommonAttackSurfaces'
        allowed_domains = ['http://capec.mitre.org/']
        namespaces = [("capec", "http://capec.mitre.org/capec-2")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("capec_v2.8.xml")
        start_urls = [filepath]
        itertag = 'capec:Common_Attack_Surface'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECPostPipeline': 980,
            # 'attackKB_crawler.pipelines.capec_pipelines.CapecMitreCommonAttackSurfacesMySQLStorePipeline': 932,
            # 'attackKB_crawler.pipelines.capec_pipelines.CAPECCommonAttackSurfacesJsonWriterPipeline': 900,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CapecMitreSpider_CommonAttackSurfaces, self).__init__(*args, **kwargs)
            self.callback = callback

        def parse_node(self, response, node):
            self.logger.info("CAPEC Common_Attack_Surfaces Node")
            item = CapecMitreCommonAttackSurfacesItems()
            item['callback'] = self.callback
            item['Capec_Type'] = "Common_Attack_Surfaces"
            item['Target_Attack_Surface_DescriptionType'] = ",".join([str(i) for i in target_attack_surface_descriptiontype(self, node)])
            item['Common_Attack_Surface_ID'] = ",".join([s for s in node.xpath('@ID').extract()])
