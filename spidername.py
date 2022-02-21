
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
import requests,json
from server_setting import get_server_info


server = get_server_info()
url = server.get_url()
headers = server.get_headers()
process = CrawlerRunner(get_project_settings())
spiders = []
for spider in process.spider_loader.list():
    spiders.append(spider)
spider = {}
spiderlist =[]
for item in  spiders:
    spider["name"] = item
    spiderlist.append(spider)


r = requests.post(url, data=json.dumps(spiderlist), headers=headers)
r.status_code
r.text
