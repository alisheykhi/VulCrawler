import scrapy,os
import base64
from attackKB_crawler.info2cpe.api import search_cpe

from attackKB_crawler.items.cve_items import CVEItems

class SecurityFocusSpider(scrapy.Spider):

    name                = 'Security_Focus'
    allowed_domains     = ['securityfocus.com']
    tabs_name = {'info':'info','discuss':'discuss', 'exploit':'exploit', 'solution':'solution', 'references':'references'}
    custom_settings     = {
        'ITEM_PIPELINES': {
            'attackKB_crawler.pipelines.post_pipeline.PostPipeline': 901,
            #'attackKB_crawler.pipelines.securityfocus_pipelines.SecurityFocusMySQLStorePipeline': 932,
            #'attackKB_crawler.pipelines.securityfocus_pipelines.SecurityFocusJsonWriterPipeline': 900,
        },
        #'FILES_STORE' : '/SecurityFocus_File/Exploit_file'
    }
    update_list = []
    xpath ={"info_id":"//div[@id='vulnerability']/table/tr/td//text()",
            "title":"//span[@class='title']/text()",
             "cve":"//div[@id='vulnerability']/table/tr[@valign='top'][1]/td//text()",
             "vulnerable":"//div[@id='vulnerability']/table/tr[@valign='top'][2]/td//text()",
             "not_vulnerable":"//div[@id='vulnerability']/table/tr[@valign='top'][3]/td//text()",
             "discuss":"//div[@id='vulnerability']/text()",
            "exploit_file":"//div[@id='vulnerability']/ul/li/a/@href",
            "reference_title": "//div[@id='vulnerability']/ul/li/a/text()"}

    def __init__(self, callback, lbid = 1, fbid = 1, update_list= [] ,*args, **kwargs):
        super(SecurityFocusSpider, self).__init__(*args, **kwargs)
        self.last_bid   =  int (lbid)
        self.first_bid  =  int (fbid)
        self.update_list=  update_list
        self.callback = callback

    def start_requests(self):
        if self.update_list:
            for link in self.update_list:
                yield scrapy.Request(link , self.parse_info)
        else:
            for bid in range(self.first_bid, self.last_bid+1):
                yield scrapy.Request('http://www.securityfocus.com/bid/%s' % bid , self.parse_info)

    def parse_info(self, response):
        self.logger.info("Security Focus item")
        if response.status < 400 :
            self.logger.info("Bugtraq item ...")
            item        = CVEItems()
            item_name   = ['Bugtraq ID:','Class:','Remote:','Local:','Published:','Updated:','Credit:']
            item['URL'] = response.url
            td_range    = len(response.xpath(self.xpath['info_id']).extract())

            for i in range(0, td_range):
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[0]:
                    item['Bugtraq_ID']  = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[1]:
                    item['Class']       = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[2]:
                    item['Remote']      = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[3]:
                    item['Local']       = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[4]:
                    item['Published']   = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[5]:
                    item['Modified']     = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()
                if (str(response.xpath(self.xpath['info_id']).extract()[i]).strip()) == item_name[6]:
                    item['Credit']      = str(response.xpath(self.xpath['info_id']).extract()[i+2]).strip()

            item['Title']           = str(response.xpath(self.xpath['title']).extract()[0])
            item['CVE_ID']             = ",".join([ s.replace("CVE:","").strip() for s in response.xpath(self.xpath['cve']).extract()]).strip(",")
            Vulnerable = [ s.replace("Vulnerable:","").strip() for s in response.xpath(self.xpath['vulnerable']).extract()]
            cpe_format = []
            for vulnerable in Vulnerable:
                cpe = search_cpe(vulnerable)
                cpe_format.append(cpe)
            item['Vulnerable'] = cpe_format
            cpe_format = []
            Not_Vulnerable = ([s.replace("Not Vulnerable:", "").strip() for s in response.xpath(self.xpath['not_vulnerable']).extract()])
            for not_vulnerable in Not_Vulnerable:
                cpe = search_cpe(not_vulnerable)
                cpe_format.append(cpe)
            item['Not_Vulnerable'] = cpe_format
            url                     = response.url + '/' + self.tabs_name['discuss']
            request                 = scrapy.Request(url, self.parse_discuss)
            request.meta['item']    = item
            yield request
        else:
            print "___________________________\n"
            print "  no bug_traq_id for :" + response.url + "\n"
            print "___________________________\n"
            return

    def parse_discuss(self, response):
        item = response.meta['item']
        item['Description']         = "\n".join([ s.strip() for s in response.xpath(self.xpath['discuss']).extract()]).strip(",")
        url                     = str(response.url).replace(self.tabs_name['discuss'], self.tabs_name['exploit'])
        request                 = scrapy.Request(url, self.parse_exploit)
        request.meta['item']    = item
        yield request

    def parse_exploit(self, response):
        exploit_file_name = []
        item = response.meta['item']
        exploit = "\n".join([ s.strip() for s in response.xpath(self.xpath['discuss']).extract()]).strip(",")
        if exploit!="\n":
            item['Exploit_Description']= "\n".join([ s.strip() for s in response.xpath(self.xpath['discuss']).extract()]).strip(",")
        for file_url in response.xpath(self.xpath['exploit_file']).extract():
            exploit_file_name.append(file_url.split("/")[-1])
            url = "http://www.securityfocus.com"+str(file_url)
            req_for_file = scrapy.Request (url, self.save_exploit_file)
            req_for_file.meta['item'] = item
            yield req_for_file

        item['Exploit_file_name']    = ",".join(exploit_file_name)

        url                     = str(response.url).replace(self.tabs_name['exploit'], self.tabs_name['solution'])
        request                 = scrapy.Request(url, self.parse_solution)
        request.meta['item']    = item
        yield request

    def parse_solution(self, response):
        solution_file_name = []
        item = response.meta['item']
        solution =  "\n".join([s.strip() for s in response.xpath(self.xpath['discuss']).extract()]).strip(",")
        if solution!= "\n":
            item['Solution_Description'] = solution
        for file_url in response.xpath(self.xpath['exploit_file']).extract():
            solution_file_name.append(file_url.split("/")[-1])
            url = str(file_url)
            req_for_file = scrapy.Request(url, self.save_patch_file)
            req_for_file.meta['item'] = item
            yield req_for_file


        item['Solution_file_name'] = ",".join(solution_file_name)
        url = str(response.url).replace(self.tabs_name['solution'], self.tabs_name['references'])
        request = scrapy.Request(url, self.parse_references)
        request.meta['item'] = item
        yield request

    def parse_references(self, response):
        item                    = response.meta['item']
        references = []
        References_title = response.xpath(self.xpath['reference_title']).extract()
        References_link = response.xpath(self.xpath['exploit_file']).extract()
        number_of_reference = len(References_title)
        for index in range (0,number_of_reference):
            references.append({"Reference_Name" :References_title[index]  ,"References_link": References_link[index]})
        item['References']= references
        item['callback'] = self.callback
        yield item

    def save_exploit_file(self, response):
        item                   = response.meta['item']
        #path = "//SecurityFocus_file/Exploit_file/"
        directory = os.getcwd()+"/SecurityFocus_File/Exploit_file/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = directory+str(response.url).split("/")[-1]
        com = base64.b64encode(response.body)
        with open(path, "wb") as f:
            f.write(com)
        item['Exploit_file'] = com



    def save_patch_file(self, response):
        item = response.meta['item']
        # path = "//SecurityFocus_file/Exploit_file/"
        directory = os.getcwd() + "/SecurityFocus_File/Patch_file/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = directory + str(response.url).split("/")[-1]
        com = base64.b64encode(response.body)
        with open(path, "wb") as f:
            f.write(response.body)
        item['Solution_file'] = com