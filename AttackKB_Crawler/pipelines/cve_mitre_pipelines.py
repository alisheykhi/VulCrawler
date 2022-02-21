# -*- coding: utf-8 -*-
import codecs
import json
import MySQLdb
from collections import OrderedDict
from scrapy.exceptions import DropItem


def tonull(param):
    if param == "":
        return None
    else:
        return param

class CVEMitreMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="usercve", passwd="123", db="CVE_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO `cve` (`URL`, `CVE_ID`, `Bugtraq_ID`, `Description`, `Published`,"
                                "`Modified`, `Status`, `Source`, `Class`, `CVSS_Severity_version3`, `CVSS_Severity_version2`, `CVSS_Version3_Metrics`, `CVSS_Version2_Metrics`,"
                                "`Vulnerable`, `Not_Vulnerable`,`Exploit`,`Exploit_file`,`Solution`, `Patch_file`, `Remote`, `Local`, `Credit`, `Technical_Details`, `References`)"
                                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (tonull(item['URL'].encode('utf-8')),
                                 tonull(item['CVE_ID'].encode('utf-8')),
                                 tonull(item['Bugtraq_ID'].encode('utf-8')),
                                 tonull(item['Description'].encode('utf-8')),
                                 tonull(item['Published'].encode('utf-8')),
                                 tonull(item['Modified'].encode('utf-8')),
                                 tonull(item['Status'].encode('utf-8')),
                                 tonull(item['Source'].encode('utf-8')),
                                 tonull(item['Class'].encode('utf-8')),
                                 tonull(item['CVSS_Severity_version3'].encode('utf-8')),
                                 tonull(item['CVSS_Severity_version2'].encode('utf-8')),
                                 tonull(item['CVSS_Version3_Metrics'].encode('utf-8')),
                                 tonull(item['CVSS_Version2_Metrics'].encode('utf-8')),
                                 tonull(item['Vulnerable'].encode('utf-8')),
                                 tonull(item['Not_Vulnerable'].encode('utf-8')),
                                 tonull(item['Exploit'].encode('utf-8')),
                                 tonull(item['Exploit_file'].encode('utf-8')),
                                 tonull(item['Solution'].encode('utf-8')),
                                 tonull(item['Patch_file'].encode('utf-8')),
                                 tonull(item['Remote'].encode('utf-8')),
                                 tonull(item['Local'].encode('utf-8')),
                                 tonull(item['Credit'].encode('utf-8')),
                                 tonull(item['Technical_Details'].encode('utf-8')),
                                 tonull(item['References'].encode('utf-8'))))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


class CVEMitreJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('cve-mitre-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item
