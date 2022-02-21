import scrapy

class CVEItems(scrapy.Item):

    URL = scrapy.Field()  # Page URL
    Title = scrapy.Field() # Title (Security_Focus)
    CVE_ID = scrapy.Field()  # CVE_ID(CVE_Mitre)/Vul_ID(NVD)/CVE(Security_Focuse)
    Bugtraq_ID = scrapy.Field()  # Bugtraq_ID(Security Focuse)
    Description = scrapy.Field()  # Description(CVE_Mitre)/Overview(CVE_NVD)/Discussion(Security_Focuse)
    Published = scrapy.Field()  # Published(CVE_Mitre)/Original_Release_Date(CVE NVD)/Published(Security Focuse)
    Modified = scrapy.Field()  # Modified(CVE_Mitre)/Last_Revised(CVE_NVD)/Updated(Security Focuse)
    Status = scrapy.Field()  # CVE Mitre
    Source = scrapy.Field()  # CVE_NVD
    Class = scrapy.Field()  # Class(Security Focuse)
    CVSS_Severity_version3 = scrapy.Field()  # Impact(CVE NVD)
    CVSS_Severity_version2 = scrapy.Field()  # Impact(CVE NVD)
    CVSS_Version3_Metrics = scrapy.Field()  # Impact(CVE NVD)
    CVSS_Version2_Metrics = scrapy.Field()  # Impact(CVE NVD)
    Vulnerable = scrapy.Field()  # Vulnerable(Security Focuse)/Vulnerable_Software_Versions(CVE_NVD)
    Not_Vulnerable = scrapy.Field()  # Not_Vulnerable(Security Focuse)
    Exploit_Description = scrapy.Field()  # Exploit(Security Focuse)
    Exploit_file_name = scrapy.Field()  # Exploit_file(Security Focuse)
    Exploit_file = scrapy.Field()
    Solution_Description = scrapy.Field()  # Solution(Security Focuse)
    Solution_file_name = scrapy.Field()  # Patch_file(Security Focuse)
    Solution_file = scrapy.Field()
    Remote = scrapy.Field()  # Remote(Security Focuse)
    Local = scrapy.Field()  # Local(Security Focuse)
    Credit = scrapy.Field()  # Credit(Security Focuse)
    Technical_Details = scrapy.Field()  # nvd (Technical_Details(CVE_NVD))
    References = scrapy.Field()
    callback = scrapy.Field()



    # Reference_Name = scrapy.Field()  # References_title(Security Focuse)/References_Description(CVE Mitre)/External_Sources(CVE_NVD)
    # Reference_Eternal_Source = scrapy.Field()  # External_Sources(CVE_NVD)
    # US_CERT_Vulnerability_Note = scrapy.Field()  # External_Sources(CVE_NVD)
    # References_Type = scrapy.Field()  # External_Sources(CVE_NVD)
    # References_link = scrapy.Field()  # External_Sources(CVE_NVD)/References_URL(CVE Mitre)/References_link(Security Focuse)

