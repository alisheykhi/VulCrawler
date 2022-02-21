
import scrapy

class CVEItem(scrapy.Item):
    URL                    = scrapy.Field() #Page URL
    CVE_ID                 = scrapy.Field() #CVE_ID(CVE_Mitre)/Vul_ID(NVD)/CVE(Security_Focuse)
    Bugtraq_ID             = scrapy.Field() #Bugtraq_ID(Security Focuse)
    Description            = scrapy.Field() #Description(CVE_Mitre)/Overview(CVE_NVD)/Discussion(Security_Focuse)
    Published              = scrapy.Field() #Published(CVE_Mitre)/Original_Release_Date(CVE NVD)/Published(Security Focuse)
    Modified               = scrapy.Field() #Modified(CVE_Mitre)/Last_Revised(CVE_NVD)/Updated(Security Focuse)
    Status                 = scrapy.Field() #CVE Mitre
    Source                 = scrapy.Field() #CVE_NVD
    Class                  = scrapy.Field() #Class(Security Focuse)
    CVSS_Severity_version3 = scrapy.Field() #Impact(CVE NVD)
    CVSS_Severity_version2 = scrapy.Field() #Impact(CVE NVD)
    CVSS_Version3_Metrics  = scrapy.Field() #Impact(CVE NVD)
    CVSS_Version2_Metrics  = scrapy.Field() #Impact(CVE NVD)
    Vulnerable             = scrapy.Field() #Vulnerable(Security Focuse)/Vulnerable_Software_Versions(CVE_NVD)
    Not_Vulnerable         = scrapy.Field() #Not_Vulnerable(Security Focuse)
    Exploit                = scrapy.Field() #Exploit(Security Focuse)
    Exploit_file           = scrapy.Field() #Exploit_file(Security Focuse)
    Solution               = scrapy.Field() #Solution(Security Focuse)
    Patch_file             = scrapy.Field() #Patch_file(Security Focuse)
    Remote                 = scrapy.Field() #Remote(Security Focuse)
    Local                  = scrapy.Field() #Local(Security Focuse)
    Credit                 = scrapy.Field() #Credit(Security Focuse)
    Technical_Details      = scrapy.Field() #Technical_Details(CVD_NVD)
    References             = scrapy.Field()
    callback = scrapy.Field()
    #References contain five field :
        # Reference_Name         = scrapy.Field()
        # Reference_Eternal_Source = scrapy.Field()
        # US_CERT_Vulnerability_Note = scrapy.Field()
        # References_Type        = scrapy.Field()
        # References_link        = scrapy.Field()



    #***************** CVE Mitre ***********
    #CVE_ID                 =   scrapy.Field()
    #Description            =   scrapy.Field()
    #Published              =   scrapy.Field()
    #Modified               =   scrapy.Field()
    #Status                 =   scrapy.Field()
    #References_URL         =   scrapy.Field()
    #References_Description =   scrapy.Field()

    #***************** CVE NVD *************
    #url                   = scrapy.Field()
    #Vul_ID                = scrapy.Field()
    #Original_Release_Date = scrapy.Field()
    #Last_Revised          = scrapy.Field()
    #Source                = scrapy.Field()
    #Overview              = scrapy.Field()
    #Impact                = scrapy.Field()
    #Referencesto_Advisories_Solutions_Tools = scrapy.Field() #Ignore
    #External_Sources        = scrapy.Field()
    #Vulnerable_Software_Versions = scrapy.Field()
    #Technical_Details     = scrapy.Field()

    #***************** Security Focuse *****
    #Bugtraq_ID          =   scrapy.Field()
    #Title               =   scrapy.Field()
    #Class               =   scrapy.Field()
    #CVE                 =   scrapy.Field()
    #Remote              =   scrapy.Field()
    #Local               =   scrapy.Field()
    #Published           =   scrapy.Field()
    #Updated             =   scrapy.Field()
    #Credit              =   scrapy.Field()
    #Vulnerable          =   scrapy.Field()
    #Not_Vulnerable      =   scrapy.Field()
    #Discuss             =   scrapy.Field()
    #Exploit             =   scrapy.Field()
    #Exploit_file        =   scrapy.Field()
    #Solution            =   scrapy.Field()
    #Patch_file          =   scrapy.Field()
    #References_title    =   scrapy.Field()
    #References_link     =   scrapy.Field()
    #url                 =   scrapy.Field()




