import json
import MySQLdb
import requests

#import codecs
#from collections import OrderedDict
#from scrapy.exceptions import DropItem

class SecurityFocusMySQLStorePipeline(object):
    def __init__(self):
      self.conn = MySQLdb.connect(user="root", passwd="", db="sf", host="127.0.0.1", charset="utf8", use_unicode=True)
      self.cursor = self.conn.cursor()


    def process_item(self, item, spider):
        print "______________________________________________________________________________"
        for key, val in spider.crawler.stats.get_stats().items():
            print key, ":", val
        print "______________________________________________________________________________"

        try:
            self.cursor.execute("INSERT INTO `cve` (`Bugtraq_ID`, `Title`, `Class`, `CVE`, `Remote`,"
                                   " `Local`, `Published`, `Updated`, `Credit`, `Vulnerable`, `Not_Vulnerable`,"
                                   " `Discuss`, `Exploit`, `Exploit_file`, `Solution`, `Patch_file`, `References_title`"
                                   ", `References_link`, `url`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                   (item['Bugtraq_ID'].encode('utf-8'),
                                    item['Title'].encode('utf-8'),
                                    item['Class'].encode('utf-8'),
                                    item['CVE'].encode('utf-8'),
                                    item['Remote'].encode('utf-8'),
                                    item['Local'].encode('utf-8'),
                                    item['Published'].encode('utf-8'),
                                    item['Updated'].encode('utf-8'),
                                    item['Credit'].encode('utf-8'),
                                    item['Vulnerable'].encode('utf-8'),
                                    item['Not_Vulnerable'].encode('utf-8'),
                                    item['Discuss'].encode('utf-8'),
                                    item['Exploit'].encode('utf-8'),
                                    item['Exploit_file'].encode('utf-8'),
                                    item['Solution'].encode('utf-8'),
                                    item['Patch_file'].encode('utf-8'),
                                    ",".join(item['References_title']).encode('utf-8'),
                                    ",".join(item['References_link']).encode('utf-8'),
                                    item['url'].encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


    def close_spider(self, spider):
        print "________________________________from pipeline________________________________"
        #print spider.crawler.stats.get_stats()
        for key,val in spider.crawler.stats.get_stats().items():
            print key,":",val
        print "______________________________________________________________________________"

class SecurityFocusJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('security-focus-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        del item['callback']
        line = json.dumps(dict(item), indent=4, sort_keys=False, encoding="ISO-8859-1")+ "\n"
        self.file.write(line)
        return item

class SecurityFocusPostPipeline(object):

    def __init__(self):
        self.url = "http://localhost:8000/postreq/"
        self.headers = {'content-type': 'application/json'}

    def process_item(self, item, spider):
        print "______________________________________________________________________________"
        for key, val in spider.crawler.stats.get_stats().items():
            print key, ":", val
        print "______________________________________________________________________________"
        data = {'Bugtraq_ID' : item['Bugtraq_ID']},{'Title' : item['Title']},{'url' : item['url']}
        r = requests.post(self.url, data=json.dumps(data), headers=self.headers)
        r.status_code
        r.text
        return item

    def close_spider(self, spider):
        print "________________________________from pipeline________________________________"
        # print spider.crawler.stats.get_stats()
        for key, val in spider.crawler.stats.get_stats().items():
            print key, ":", val
        print "______________________________________________________________________________"


class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('security-focus-Encoding.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False ) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

'''
class MongoDBPipeline(object):
    def __init__(self):
        import pymongo
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        self.db = connection[settings['MONGODB_DB']]
        self.collection = self.db[settings['MONGODB_COLLECTION']]
        if self.__get_uniq_key() is not None:
            self.collection.create_index(self.__get_uniq_key(), unique=True)

    def process_item(self, item, spider):
        if self.__get_uniq_key() is None:
            self.collection.insert(dict(item))
        else:
            self.collection.update(
                            {self.__get_uniq_key(): item[self.__get_uniq_key()]},
                            dict(item),
                            upsert=True)
        log.msg("Item wrote to MongoDB database %s/%s" %
                    (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
        return item

    def __get_uniq_key(self):
        if not settings['MONGODB_UNIQ_KEY'] or settings['MONGODB_UNIQ_KEY'] == "":
            return None
        return settings['MONGODB_UNIQ_KEY']

'''

