import json
import MySQLdb

class CWEMitreViewMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="root", passwd="", db="cwe", host="127.0.0.1", charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `view` (`CWE_Type`, `CWE_ID`, `CWE_Name`, `CWE_status`, `View_Structure`, `View_Objective`, `View_Audience`,"
                "`View_Filter`, `Relationships`, `Relationship_Notes`, `Maintenance_Notes`,"
                "`Other_Notes`, `Alternate_Terms`, `Research_Gaps`, `References`, `Content_History`) "
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item['CWE_Type'].encode('utf-8'),
                 item['CWE_ID'].encode('utf-8'),
                 item['CWE_Name'].encode('utf-8'),
                 item['CWE_status'].encode('utf-8'),
                 item['View_Structure'].encode('utf-8'),
                 item['View_Objective'].encode('utf-8'),
                 item['View_Audience'].encode('utf-8'),
                 item['View_Filter'].encode('utf-8'),
                 item['Relationships'].encode('utf-8'),
                 item['Relationship_Notes'].encode('utf-8'),
                 item['Maintenance_Notes'].encode('utf-8'),
                 item['Other_Notes'].encode('utf-8'),
                 item['Alternate_Terms'].encode('utf-8'),
                 item['Research_Gaps'].encode('utf-8'),
                 item['References'].encode('utf-8'),
                 item['Content_History'].encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CWEMitreCategoryMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="root", passwd="", db="cwe", host="127.0.0.1", charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `category` (`CWE_Type`, `CWE_ID`, `CWE_Name`, `CWE_status`, `Description`,"
                "`Relationships`, `Relationship_Notes`, `Weakness_Ordinalities`, `Applicable_Platforms`,"
                "`Maintenance_Notes`, `Background_Details`, `Other_Notes`, `Alternate_Terms`, `Terminology_Notes`, `Time_of_Introduction`, `Modes_of_Introduction`, `Enabling_Factors_for_Exploitation`,"
                "`Likelihood_of_Exploit`, `Common_Consequences`, `Detection_Methods`, `Potential_Mitigations`, `Causal_Nature`,"
                "`Demonstrative_Examples`, `Observed_Examples`, `Theoretical_Notes`, `Functional_Areas`, `Relevant_Properties`, `Affected_Resources`,"
                "`Research_Gaps`, `References`, `Taxonomy_Mappings`, `White_Box_Definitions`, `Black_Box_Definitions`, `Related_Attack_Patterns`, `Content_History`) "
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",
                (str(item['CWE_Type']).encode('utf-8'),
                 str(item['CWE_ID']).encode('utf-8'),
                 str(item['CWE_Name']).encode('utf-8'),
                 str(item['CWE_status']).encode('utf-8'),
                 str(item['Description']).encode('utf-8'),
                 str(item['Relationships']).encode('utf-8'),
                 str(item['Relationship_Notes']).encode('utf-8'),
                 str(item['Weakness_Ordinalities']).encode('utf-8'),
                 str(item['Applicable_Platforms']).encode('utf-8'),
                 str(item['Maintenance_Notes']).encode('utf-8'),
                 str(item['Background_Details']).encode('utf-8'),
                 str(item['Other_Notes']).encode('utf-8'),
                 str(item['Alternate_Terms']).encode('utf-8'),
                 str(item['Terminology_Notes']).encode('utf-8'),
                 str(item['Time_of_Introduction']).encode('utf-8'),
                 str(item['Modes_of_Introduction']).encode('utf-8'),
                 str(item['Enabling_Factors_for_Exploitation']).encode('utf-8'),
                 str(item['Likelihood_of_Exploit']).encode('utf-8'),
                 str(item['Common_Consequences']).encode('utf-8'),
                 str(item['Detection_Methods']).encode('utf-8'),
                 str(item['Potential_Mitigations']).encode('utf-8'),
                 str(item['Causal_Nature']).encode('utf-8'),
                 str(item['Demonstrative_Examples']).encode('utf-8'),
                 str(item['Observed_Examples']).encode('utf-8'),
                 str(item['Theoretical_Notes']).encode('utf-8'),
                 str(item['Functional_Areas']).encode('utf-8'),
                 str(item['Relevant_Properties']).encode('utf-8'),
                 str(item['Affected_Resources']).encode('utf-8'),
                 str(item['Research_Gaps']).encode('utf-8'),
                 str(item['References']).encode('utf-8'),
                 str(item['Taxonomy_Mappings']).encode('utf-8'),
                 str(item['White_Box_Definitions']).encode('utf-8'),
                 str(item['Black_Box_Definitions']).encode('utf-8'),
                 str(item['Related_Attack_Patterns']).encode('utf-8'),
                 str(item['Content_History']).encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CWEMitreCompoundElementMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="root", passwd="", db="cwe", host="127.0.0.1", charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `compoundelement` (`CWE_Type`, `CWE_ID`, `CWE_Name`, `CWE_status`, `Compound_Element_Abstraction`, `Compound_Element_Structure`, `Description`,"
                "`Relationships`, `Relationship_Notes`, `Weakness_Ordinalities`, `Applicable_Platforms`,"
                "`Maintenance_Notes`, `Background_Details`, `Other_Notes`, `Alternate_Terms`, `Terminology_Notes`, `Time_of_Introduction`, `Modes_of_Introduction`, `Enabling_Factors_for_Exploitation`,"
                "`Likelihood_of_Exploit`, `Common_Consequences`, `Detection_Methods`, `Potential_Mitigations`, `Causal_Nature`,"
                "`Demonstrative_Examples`, `Observed_Examples`, `Theoretical_Notes`, `Functional_Areas`, `Relevant_Properties`, `Affected_Resources`,"
                "`Research_Gaps`, `References`, `Taxonomy_Mappings`, `White_Box_Definitions`, `Black_Box_Definitions`, `Related_Attack_Patterns`, `Content_History`) "
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",
                (str(item['CWE_Type']).encode('utf-8'),
                 str(item['CWE_ID']).encode('utf-8'),
                 str(item['CWE_Name']).encode('utf-8'),
                 str(item['CWE_status']).encode('utf-8'),
                 str(item['Compound_Element_Abstraction']).encode('utf-8'),
                 str(item['Compound_Element_Structure']).encode('utf-8'),
                 str(item['Description']).encode('utf-8'),
                 str(item['Relationships']).encode('utf-8'),
                 str(item['Relationship_Notes']).encode('utf-8'),
                 str(item['Weakness_Ordinalities']).encode('utf-8'),
                 str(item['Applicable_Platforms']).encode('utf-8'),
                 str(item['Maintenance_Notes']).encode('utf-8'),
                 str(item['Background_Details']).encode('utf-8'),
                 str(item['Other_Notes']).encode('utf-8'),
                 str(item['Alternate_Terms']).encode('utf-8'),
                 str(item['Terminology_Notes']).encode('utf-8'),
                 str(item['Time_of_Introduction']).encode('utf-8'),
                 str(item['Modes_of_Introduction']).encode('utf-8'),
                 str(item['Enabling_Factors_for_Exploitation']).encode('utf-8'),
                 str(item['Likelihood_of_Exploit']).encode('utf-8'),
                 str(item['Common_Consequences']).encode('utf-8'),
                 str(item['Detection_Methods']).encode('utf-8'),
                 str(item['Potential_Mitigations']).encode('utf-8'),
                 str(item['Causal_Nature']).encode('utf-8'),
                 str(item['Demonstrative_Examples']).encode('utf-8'),
                 str(item['Observed_Examples']).encode('utf-8'),
                 str(item['Theoretical_Notes']).encode('utf-8'),
                 str(item['Functional_Areas']).encode('utf-8'),
                 str(item['Relevant_Properties']).encode('utf-8'),
                 str(item['Affected_Resources']).encode('utf-8'),
                 str(item['Research_Gaps']).encode('utf-8'),
                 str(item['References']).encode('utf-8'),
                 str(item['Taxonomy_Mappings']).encode('utf-8'),
                 str(item['White_Box_Definitions']).encode('utf-8'),
                 str(item['Black_Box_Definitions']).encode('utf-8'),
                 str(item['Related_Attack_Patterns']).encode('utf-8'),
                 str(item['Content_History']).encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

class CWEMitreWeaknessMySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user="root", passwd="", db="cwe", host="127.0.0.1", charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                "INSERT INTO `weakness` (`CWE_Type`, `CWE_ID`, `CWE_Name`, `CWE_status`, `Weakness_Abstraction`, `Description`,"
                "`Relationships`, `Relationship_Notes`, `Weakness_Ordinalities`, `Applicable_Platforms`,"
                "`Maintenance_Notes`, `Background_Details`, `Other_Notes`, `Alternate_Terms`, `Terminology_Notes`, `Time_of_Introduction`, `Modes_of_Introduction`, `Enabling_Factors_for_Exploitation`,"
                "`Likelihood_of_Exploit`, `Common_Consequences`, `Detection_Methods`, `Potential_Mitigations`, `Causal_Nature`,"
                "`Demonstrative_Examples`, `Observed_Examples`, `Theoretical_Notes`, `Functional_Areas`, `Relevant_Properties`, `Affected_Resources`,"
                "`Research_Gaps`, `References`, `Taxonomy_Mappings`, `White_Box_Definitions`, `Black_Box_Definitions`, `Related_Attack_Patterns`, `Content_History`) "
                "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",
                (str(item['CWE_Type']).encode('utf-8'),
                 str(item['CWE_ID']).encode('utf-8'),
                 str(item['CWE_Name']).encode('utf-8'),
                 str(item['CWE_status']).encode('utf-8'),
                 str(item['Weakness_Abstraction']).encode('utf-8'),
                 str(item['Description']).encode('utf-8'),
                 str(item['Relationships']).encode('utf-8'),
                 str(item['Relationship_Notes']).encode('utf-8'),
                 str(item['Weakness_Ordinalities']).encode('utf-8'),
                 str(item['Applicable_Platforms']).encode('utf-8'),
                 str(item['Maintenance_Notes']).encode('utf-8'),
                 str(item['Background_Details']).encode('utf-8'),
                 str(item['Other_Notes']).encode('utf-8'),
                 str(item['Alternate_Terms']).encode('utf-8'),
                 str(item['Terminology_Notes']).encode('utf-8'),
                 str(item['Time_of_Introduction']).encode('utf-8'),
                 str(item['Modes_of_Introduction']).encode('utf-8'),
                 str(item['Enabling_Factors_for_Exploitation']).encode('utf-8'),
                 str(item['Likelihood_of_Exploit']).encode('utf-8'),
                 str(item['Common_Consequences']).encode('utf-8'),
                 str(item['Detection_Methods']).encode('utf-8'),
                 str(item['Potential_Mitigations']).encode('utf-8'),
                 str(item['Causal_Nature']).encode('utf-8'),
                 str(item['Demonstrative_Examples']).encode('utf-8'),
                 str(item['Observed_Examples']).encode('utf-8'),
                 str(item['Theoretical_Notes']).encode('utf-8'),
                 str(item['Functional_Areas']).encode('utf-8'),
                 str(item['Relevant_Properties']).encode('utf-8'),
                 str(item['Affected_Resources']).encode('utf-8'),
                 str(item['Research_Gaps']).encode('utf-8'),
                 str(item['References']).encode('utf-8'),
                 str(item['Taxonomy_Mappings']).encode('utf-8'),
                 str(item['White_Box_Definitions']).encode('utf-8'),
                 str(item['Black_Box_Definitions']).encode('utf-8'),
                 str(item['Related_Attack_Patterns']).encode('utf-8'),
                 str(item['Content_History']).encode('utf-8')))

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item


class CWEViewJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('CWEView-prettyprint.json', 'wb')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CWECategoryJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('CWECategory-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CWECompoundElementJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('CWECompoundElement-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item

class CWEWeaknessJsonWriterPipeline(object):
    def __init__(self):
        self.file = open('CWEWeakness-prettyprint.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), indent=4, sort_keys=False) + "\n"
        self.file.write(line)
        return item
