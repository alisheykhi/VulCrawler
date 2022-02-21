
import scrapy



class SecurityFocusItem(scrapy.Item):
    Bugtraq_ID          =   scrapy.Field()
    Title               =   scrapy.Field()
    Class               =   scrapy.Field()
    CVE                 =   scrapy.Field()
    Remote              =   scrapy.Field()
    Local               =   scrapy.Field()
    Published           =   scrapy.Field()
    Updated             =   scrapy.Field()
    Credit              =   scrapy.Field()
    Vulnerable          =   scrapy.Field()
    Not_Vulnerable      =   scrapy.Field()
    Discuss             =   scrapy.Field()
    Exploit             =   scrapy.Field()
    Exploit_file        =   scrapy.Field()
    Solution            =   scrapy.Field()
    Patch_file          =   scrapy.Field()
    References_title    =   scrapy.Field()
    References_link     =   scrapy.Field()
    url                 =   scrapy.Field()
    callback            =   scrapy.Field()


