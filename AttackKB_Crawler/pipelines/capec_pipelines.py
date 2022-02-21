
import json
import MySQLdb
import requests


class CapecMitreAttackPatternMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:

            self.cursor.execute("INSERT INTO `attackpattern` (`Capec_Type`, `Capec_ID`,`Capec_Name`,`Capec_status`, `Capec_Pattern_Abstraction`,`Capec_Pattern_Completeness`, `Description`,"
                                "`Alternate_Terms`,`Target_Attack_Surface`, `Attack_Prerequisites`,`Typical_Severity`,`Typical_Likelihood_of_Exploit`, `Methods_of_Attack`,"
                                "`Examples_Instances`,`Attacker_Skills_or_Knowledge_Required`,`Resources_Required`, `Probing_Techniques`, `Indicators_Warnings_of_Attack`,"
                                "`Obfuscation_Techniques`,`Solutions_and_Mitigations`,`Attack_Motivation_Consequences`,`Injection_Vector`,`Payload`,`Activation_Zone`,`Payload_Activation_Impact`,"
                                "`Related_Weakness`,`Related_Vulnerabilities`,`Related_Attack_Patterns`,`Relevant_Security_Requirements`,`Relevant_Design_Patterns`,`Relevant_Security_Patterns`,"
                                "`Related_Security_Principles`,`Related_Guidelines`,`Purposes`,`CIA_Impact`,`Technical_Context`,`Keywords`,`References`,`Other_Notes`,`Maintenance_Notes`,`Content_History`) "
                                "VALUES (  %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s)",
                                (item['Capec_Type'].encode('utf-8'),
                                 item['Capec_ID'].encode('utf-8'),
                                 item['Capec_Name'].encode('utf-8'),
                                 item['Capec_status'].encode('utf-8'),
                                 item['Capec_Pattern_Abstraction'].encode('utf-8'),
                                 item['Capec_Pattern_Completeness'].encode('utf-8'),
                                 item['Description'].encode('utf-8'),
                                 item['Alternate_Terms'].encode('utf-8'),
                                 item['Target_Attack_Surface'].encode('utf-8'),
                                 item['Attack_Prerequisites'].encode('utf-8'),
                                 item['Typical_Severity'].encode('utf-8'),
                                 item['Typical_Likelihood_of_Exploit'].encode('utf-8'),
                                 item['Methods_of_Attack'].encode('utf-8'),
                                 item['Examples_Instances'].encode('utf-8'),
                                 item['Attacker_Skills_or_Knowledge_Required'].encode('utf-8'),
                                 item['Resources_Required'].encode('utf-8'),
                                 item['Probing_Techniques'].encode('utf-8'),
                                 item['Indicators_Warnings_of_Attack'].encode('utf-8'),
                                 item['Obfuscation_Techniques'].encode('utf-8'),
                                 item['Solutions_and_Mitigations'].encode('utf-8'),
                                 item['Attack_Motivation_Consequences'].encode('utf-8'),
                                 item['Injection_Vector'].encode('utf-8'),
                                 item['Payload'].encode('utf-8'),
                                 item['Activation_Zone'].encode('utf-8'),
                                 item['Payload_Activation_Impact'].encode('utf-8'),
                                 item['Related_Weakness'].encode('utf-8'),
                                 item['Related_Vulnerabilities'].encode('utf-8'),
                                 item['Related_Attack_Patterns'].encode('utf-8'),
                                 item['Relevant_Security_Requirements'].encode('utf-8'),
                                 item['Relevant_Design_Patterns'].encode('utf-8'),
                                 item['Relevant_Security_Patterns'].encode('utf-8'),
                                 item['Related_Security_Principles'].encode('utf-8'),
                                 item['Related_Guidelines'].encode('utf-8'),
                                 item['Purposes'].encode('utf-8'),
                                 item['CIA_Impact'].encode('utf-8'),
                                 item['Technical_Context'].encode('utf-8'),
                                 item['Keywords'].encode('utf-8'),
                                 item['References'].encode('utf-8'),
                                 item['Other_Notes'].encode('utf-8'),
                                 item['Maintenance_Notes'].encode('utf-8'),
                                 item['Content_History'].encode('utf-8')))

            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CapecMitreCategoryMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1",charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO `category` (`Capec_Type`, `Capec_ID`,`Capec_Name`,`Capec_status`, `Description`,`Related_Weakness`,"
                                "`Attack_Prerequisite`,`Methods_of_Attack`,`Attacker_Skills_or_Knowledge_Required`, `Resources_Required`, `Attack_Motivation_Consequences`,"
                                "`Relationships`,`Relationship_Notes`,`Maintenance_Notes`,`Background_Details`,`Other_Notes`,`Alternate_Terms`,`Research_Gaps`,`References`,`Content_History`) "
                                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s )",
                                (item['Capec_Type'].encode('utf-8'),
                                 item['Capec_ID'].encode('utf-8'),
                                 item['Capec_Name'].encode('utf-8'),
                                 item['Capec_status'].encode('utf-8'),
                                 item['Description'].encode('utf-8'),
                                 item['Related_Weakness'].encode('utf-8'),
                                 item['Attack_Prerequisite'].encode('utf-8'),
                                 item['Methods_of_Attack'].encode('utf-8'),
                                 item['Attacker_Skills_or_Knowledge_Required'].encode('utf-8'),
                                 item['Resources_Required'].encode('utf-8'),
                                 item['Attack_Motivation_Consequences'].encode('utf-8'),
                                 item['Relationships'].encode('utf-8'),
                                 item['Relationship_Notes'].encode('utf-8'),
                                 item['Maintenance_Notes'].encode('utf-8'),
                                 item['Background_Details'].encode('utf-8'),
                                 item['Other_Notes'].encode('utf-8'),
                                 item['Alternate_Terms'].encode('utf-8'),
                                 item['Research_Gaps'].encode('utf-8'),
                                 item['References'].encode('utf-8'),
                                 item['Content_History'].encode('utf-8')))
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CapecMitreViewMySQLStorePipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        #print item['Capec_ID']
        #print item['View_Filter']
        try:
            self.cursor.execute("INSERT INTO `view` (`Capec_ID`, `Capec_Type`, `Capec_Name`, `Capec_status`,`View_Structure`,`View_Objective`,`View_Audience` ,`Relationships`,"
                                                    "`Relationship_Notes`,`Maintenance_Notes`,`Other_Notes` ,`Alternate_Terms`,`Research_Gaps`,`References` ,`View_Filter`,`Content_History`) "
                                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s, %s)",
                                (item['Capec_ID'].encode('utf-8'),
                                 item['Capec_Type'].encode('utf-8'),
                                 item['Capec_Name'].encode('utf-8'),
                                 item['Capec_status'].encode('utf-8'),
                                 item['View_Structure'].encode('utf-8'),
                                 item['View_Objective'].encode('utf-8'),
                                 item['View_Audience'].encode('utf-8'),
                                 item['Relationships'].encode('utf-8'),
                                 item['Relationship_Notes'].encode('utf-8'),
                                 item['Maintenance_Notes'].encode('utf-8'),
                                 item['Other_Notes'].encode('utf-8'),
                                 item['Alternate_Terms'].encode('utf-8'),
                                 item['Research_Gaps'].encode('utf-8'),
                                 item['References'].encode('utf-8'),
                                 item['View_Filter'].encode('utf-8'),
                                 item['Content_History'].encode('utf-8')))
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CapecMitreEnvironmentMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO `environment` (`Capec_Type`, `Environment_ID`,`Environment_Title`,`Environment_Description`) "
                                "VALUES ( %s, %s, %s, %s)",
                                (item['Capec_Type'].encode('utf-8'),
                                 item['Environment_ID'].encode('utf-8'),
                                 item['Environment_Title'].encode('utf-8'),
                                 item['Environment_Description'].encode('utf-8')))


            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CapecMitreCommonAttackStepsMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `commonattacksteps` (`Capec_Type`, `Custom_Attack_StepType`,`Common_Attack_Step_ID`) "
                "VALUES ( %s, %s, %s)",
                (item['Capec_Type'].encode('utf-8'),
                 item['Custom_Attack_StepType'].encode('utf-8'),
                 item['Common_Attack_Step_ID'].encode('utf-8')))
            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CapecMitreCommonAttackSurfacesMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("INSERT INTO `commonattacksurfaces` (`Capec_Type`, `Target_Attack_Surface_DescriptionType`,`Common_Attack_Surface_ID`) "
                                "VALUES ( %s, %s, %s)",
                                (item['Capec_Type'].encode('utf-8'),
                                 item['Target_Attack_Surface_DescriptionType'].encode('utf-8'),
                                 item['Common_Attack_Surface_ID'].encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CapecMitreCompoundElementsMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="UserCapec", passwd="123", db="Capec_Mitre", host="127.0.0.1", charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `compoundelements` (`Capec_Type`, `ID`,`Name`,`Compound_Element_Abstraction`, `Compound_Element_Completeness`,`Compound_Element_Structure`,"
                "`Status`,`Description`,`Relationships`, `Relationship_Notes`, `Maintenance_Notes`,"
                "`Background_Details`,`Other_Notes`,`Alternate_Terms`,`Research_Gaps`,`References`,`Content_History`) "
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s )",
                (item['Capec_Type'].encode('utf-8'),
                 item['ID'].encode('utf-8'),
                 item['Name'].encode('utf-8'),
                 item['Compound_Element_Abstraction'].encode('utf-8'),
                 item['Compound_Element_Completeness'].encode('utf-8'),
                 item['Compound_Element_Structure'].encode('utf-8'),
                 item['Status'].encode('utf-8'),
                 item['Description'].encode('utf-8'),
                 item['Relationships'].encode('utf-8'),
                 item['Relationship_Notes'].encode('utf-8'),
                 item['Maintenance_Notes'].encode('utf-8'),
                 item['Background_Details'].encode('utf-8'),
                 item['Other_Notes'].encode('utf-8'),
                 item['Alternate_Terms'].encode('utf-8'),
                 item['Research_Gaps'].encode('utf-8'),
                 item['References'].encode('utf-8'),
                 item['Content_History'].encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item



class CAPECAttackPatternJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('capec_attack_pattern-prettyprint.json', 'wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CAPECCategoryJsonWriterPipeline(object):

    def __init__(self):
        self.file = open('capec_category-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CAPECViewJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('capec_view-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CAPECEnvironmentJsonWriterPipeline(object):

    def __init__(self):
        self.file = open('capec_environment-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CAPECCommonAttackStepsJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('capec_common_attack_steps-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CAPECCommonAttackSurfacesJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('capec_common_attack_surfaces-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CAPECCompoundElementsJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('capec_compound_elements-prettyprint.json', 'wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item



