import os
from scrapy.spiders import XMLFeedSpider
from attackKB_crawler.items.cpe_items import CPEItems
import platform
from cpe import CPE


class CpeMitreSpider(XMLFeedSpider):

        name = 'CPE'
        allowed_domains = ['http://cpe.mitre.org/']
        namespaces = [("cpe-23", "http://scap.nist.gov/schema/cpe-extension/2.3")]
        pathes = {"Windows": "file:///", "Linux": "file://"}
        prefixPath = pathes.get(platform.system())
        filepath = prefixPath+os.path.abspath("official-cpe-dictionary_v2.3.xml")
        start_urls = [filepath]
        #start_urls = ["https://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml"]
        itertag = 'cpe-23:cpe23-item'
        iterator = 'xml'
        custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 980,
        },
        }

        def __init__(self, callback, *args, **kwargs):
            super(CpeMitreSpider, self).__init__(*args, **kwargs)
            self.callback = callback


        def parse_node(self, response, node):
            self.logger.info("cpe item")
            item = CPEItems()
            item['callback'] = self.callback
            cpe_name = str(node.xpath("@name").extract()[0])
            cpe_item = CPE(cpe_name)
            # item['WFN'] = cpe_item.as_wfn()
            # item['URI'] = cpe_item.as_uri_2_3()
            # item['FS'] = cpe_item.as_fs()
            # item['Dict'] = cpe_item.as_dict()
            item['name'] = cpe_item.as_fs()
            item['type'] = ",".join(cpe_item.get_part())
            item['vendor'] = ",".join(cpe_item.get_vendor())
            item['product']  = ",".join(cpe_item.get_product())
            item['version'] = ",".join(cpe_item.get_version())
            item['update'] = ",".join(cpe_item.get_update())
            item['edition'] = ",".join(cpe_item.get_edition())
            item['language'] = ",".join(cpe_item.get_language())
            item['targetSoftware'] = ",".join(cpe_item.get_target_software())
            item['targetHardware'] = ",".join(cpe_item.get_target_hardware())
            item['softwareEdition'] = ",".join(cpe_item.get_software_edition())
            item['other'] = ",".join(cpe_item.get_other())
            yield item

