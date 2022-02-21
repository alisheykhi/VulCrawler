from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import argparse
from argparse import RawTextHelpFormatter
from scrapy.crawler import CrawlerRunner
import re,platform,os




# from tqdm import *
# import time
# import threading
# import os
# from scrapy.statscollectors import StatsCollector

if platform.system()=="Linux":
    os.chdir("/home/ali/attackKB_crawler/")

def spider_list():
    spiders = []
    process = CrawlerRunner(get_project_settings())
    for spider in process.spider_loader.list():
        spiders.append(spider)
    return spiders

def run_crawler(crawlername, lbid , fbid, date, callback):
    spiders = spider_list()
    for spider in [x for x in spiders if re.search(r'^'+crawlername,x)]:
        if re.search('Security_Focus',spider):
            process.crawl(crawlername, callback, lbid=lbid, fbid=fbid )
        if re.search('Exploit_DB', spider):
            process.crawl(crawlername, callback, ldate=date)

        else:
            process.crawl(spider, callback)
    process.start()

def update_crawler(crawlername, date, callback, lbid = 2, fbid= 1):
    if re.search('Update_Security_Focus', crawlername):
        process.crawl(crawlername, callback, lbid = lbid, fbid = fbid)
    elif re.search('Update_CVE_NVD', crawlername):
        process.crawl(crawlername,callback, ladte = date)
    elif re.search('Update_CVE_Mitre', crawlername):
        process.crawl(crawlername, callback)
    elif  re.search('Exploit_DB', crawlername):
        process.crawl(crawlername, callback, ldate = date)
    process.start()




parser = argparse.ArgumentParser(description='ITRC-MT', formatter_class=RawTextHelpFormatter)
parser.add_argument('-c','--crawl', help='spider name', required=False)
parser.add_argument('-f','--firstId',type=int, help='first Bugtraq id', required=False)
parser.add_argument('-l','--lastId',type=int, help='last Bugtraq id', required=False)
parser.add_argument('-u','--Update', help='update spider', required=False,default='sf')
parser.add_argument('-d','--date', help='last update date (Format yyyy-mm-dd)', required=False)
parser.add_argument('-r','--callback', help='call back url', required=False)

args = vars(parser.parse_args())
process = CrawlerProcess(get_project_settings())
if args['crawl']:
    run_crawler(args['crawl'],lbid=args['lastId'],fbid=args['firstId'],date = args['date'],callback = args['callback'])

if args['Update']:
    update_crawler(args['Update'], lbid=args['lastId'], fbid=args['firstId'] , date = args['date'] ,callback = args['callback'])

#save_spider('cwe.xml')
#     # for i in tqdm(range(10)):
#     #     time.sleep(1)
#     #     process.start()
#     # print "Capec done!"
#     proc = (threading.Thread())
#     isDone = False
#
#     # def progress():
#     #     global proc
#     #     print "waiting"
#     #     while not proc.isDone:
#     #         print "waiting"
#
#
#     def progress():
#         global isDone
#         while not isDone:
#             print "waiting"
#         print "capec done!"
#
#     def run_process():
#         global isDone
#         isDone = False
#         print "process"
#         process.start()
#         isDone = True
#     prog = threading.Thread(target=progress(), )
#     proc = threading.Thread(target=run_process(),)
#     proc.daemon = True
#     prog.daemon = True
#     prog.start()
#     # proc.start()
#
#     # proc.join()
#
#
#     #t.daemon = True  # die if the program exits
#
#
# #exit()
