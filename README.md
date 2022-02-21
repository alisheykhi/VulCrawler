# VulCrawler!

VulCrawler is a set of crawlers that extracts structured information from almost any vulnerablitiy publisher websites.

## Extracted information

VulCrawler extracts the following attributes from vulnerablitiy publisher websites.

* Title
* Class
* CVE
* Published Date
* Vulnerable
* Exploit
* Solution
* References_link
* Patch_file
* url

## requirements:
```
scrapy
scrapy_fake_useragent
MySQLdb or MongoDB
```

## Run the crawler (via the CLI)

```
$ scrapy startproject attackKB_crawler
```
### Security Focus
```
scrapy crawl SF -a lbid=100 -a fbid=1 #crawling webpage in range (fbid,lbid). fbid = first bugtraq id and lbid = last bugtraq id
```

