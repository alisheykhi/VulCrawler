# Welcome!
## install requires:
```
scrapy
scrapy_fake_useragent
MySQLdb
```

# install

```
1. open cmd and go to working directory
2. use command "scrapy startproject attackKB_crawler"
3. open attackKB_crawler directory
4. open git Bash in current directory
5. use "git init" to initialize git repository
6. add remote git repository by "git remote add origin http://31.184.132.183/implementation/crawler.git
7. use "git pull origin master" and then enter username and pass to pull from origin
```


# Using

## Security Focus

```
scrapy crawl SF -a lbid=100 -a fbid=1 #crawling webpage in range (fbid,lbid). fbid = first bugtraq id and lbid = last bugtraq id
```