import requests
import json
import datetime
from server_setting import get_server_info


class PostPipeline(object):


    def __init__(self):
        server = get_server_info()
        self.url = server.get_url()
        self.headers = server.get_headers()
        self.started_on = datetime.datetime.now()


    def datetime_handler(self,x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    def spider_opened(self, spider):
        pass

    def process_item(self, item, spider):

        # status = spider.crawler.stats.get_stats().__dict__
        # status_req = requests.post(self.url, data=json.dumps(status), headers=self.headers)
        # status_req.status_code
        # status_req.text
        stats = spider.crawler.stats.get_stats()
        r = requests.post(self.url, data='data='+json.dumps(stats, default=self.datetime_handler), headers=self.headers)
        r.status_code
        r.text

        data = item.__dict__['_values']


        # callback = data.pop('callback')
        # r = requests.post(callback, data=json.dumps(data), headers=self.headers)
        # r.status_code
        # r.text

        return item

    def close_spider(self, spider):
        # print "________________________________from pipeline________________________________"
        # print spider.crawler.stats.get_stats()
        stats = spider.crawler.stats.get_stats()
        stats['finish_time'] = datetime.datetime.utcnow()
        stats['work_time'] = str(stats['finish_time'] - stats['start_time'])

        # print type(stats)
        # print stats
        r = requests.post(self.url, data='data='+json.dumps(stats,default = self.datetime_handler), headers=self.headers)
        #r = requests.post(self.url, data= json.dumps(stats, default=self.datetime_handler),headers=self.headers)
        r.status_code
        r.text
        # for key, val in spider.crawler.stats.get_stats().items():
        #     print key, ":", val
        # print "________________________________END______________________________________________"