
from __builtin__ import str


def structured_text_type (self, node):

    Structured_Text_Type_List=[]
    # nameSpace = '{http://capec.mitre.org/capec-2}'
    for eachnode in node:
        Structured_Text_Type_dict = {}
        Structured_Text_Type_dict["Text_Title"] = ",".join([s for s in eachnode.xpath('Text_Title/text()').extract()])
        Structured_Text_Type_dict["Text"] = ",".join([s for s in eachnode.xpath('Text/text()').extract()])
        Structured_Text_Type_dict["Code"] = ",".join([s for s in eachnode.xpath('Code/text()').extract()])
        Structured_Text_Type_dict["Comment"] = ",".join([s for s in eachnode.xpath('Comment/text()').extract()])
        Structured_Text_Type_dict["Code_Example_Language"] = ",".join([s for s in eachnode.xpath('Code_Example_Language/text()').extract()])
        Image_List = []
        for Image in eachnode.xpath('Images/Image'):
            Image_tmp = {}
            Image_tmp["Image_Location"] = ",".join([s for s in Image.xpath('Image_Location/text()').extract()])
            Image_tmp["Image_Title"] = ",".join([s for s in Image.xpath('Image_Title/text()').extract()])
            Image_List.append(dict((k, v) for k, v in Image_tmp.iteritems() if v)) if dict((k, v) for k, v in Image_tmp.iteritems() if v) !={} else None
        Structured_Text_Type_dict['Images'] = Image_List

        Structured_Text_Type_dict['Block_Nature'] = ",".join([s for s in eachnode.xpath('Block/@Block_Nature').extract()])
        Structured_Text_Type_dict["Block"] = ",".join([str(i) for i in structured_text_type(self, eachnode.xpath('Block'))])
        Structured_Text_Type_List.append(dict((k, v) for k, v in Structured_Text_Type_dict.iteritems() if v )) if dict((k, v) for k, v in Structured_Text_Type_dict.iteritems() if v ) != {} else None
    return Structured_Text_Type_List


#********************************************************************************************************
#********************************************** Common_Attributes ***************************************
#********************************************************************************************************

def Description(self,node):
    Descriptions_List = []
    Description = {}
    Description["Description_Summary"] = [s for s in node.xpath('Description_Summary/text()').extract()]
    Description["Extended_Description"] = ",".join([str(i) for i in structured_text_type(self, node.xpath('Extended_Description'))])
    Descriptions_List.append(dict((k, v) for k, v in Description.iteritems() if v)) if dict((k, v) for k, v in Description.iteritems() if v ) != {} else None
    return Descriptions_List

def Relationships(self,node):
    Relationships_List = []
    Relationships_List_Dict = {}
    for rel in node.xpath('Relationship'):
        Relationship = {}
        Relationship_View_List = []
        for view_id in rel.xpath('Relationship_Views/Relationship_View_ID'):
            Relationship_View_Dict = {}
            Relationship_View_Dict["Relationship_View_ID"] = ",".join(view_id.xpath('text()').extract())
            Relationship_View_Dict["Relationship_View_ID_Ordinal"] = ",".join(view_id.xpath('@Ordinal').extract())
            Relationship_View_List.append(dict((k, v) for k, v in Relationship_View_Dict.iteritems() if v)) if dict((k, v) for k, v in Relationship_View_Dict.iteritems() if v ) != {} else None
        Relationship["Relationship_Views"] = Relationship_View_List
        Relationship_Chains_List = []
        for chain_id in rel.xpath('Relationship_Chains/Relationship_Chain_ID'):
            Relationship_Chains_Dict = {}
            Relationship_Chains_Dict["Relationship_Chain_ID"] = ",".join(chain_id.xpath('text()').extract())
            Relationship_Chains_List.append(dict((k, v) for k, v in Relationship_Chains_Dict.iteritems() if v)) if dict((k, v) for k, v in Relationship_Chains_Dict.iteritems() if v ) != {} else None
        Relationship["Relationship_Chains"] = Relationship_Chains_List
        Relationship["Relationship_Target_Form"] = "".join(rel.xpath('Relationship_Target_Form/text()').extract())
        Relationship["Relationship_Nature"] = "".join(rel.xpath('Relationship_Nature/text()').extract())
        Relationship["Relationship_Target_ID"] = "".join(rel.xpath('Relationship_Target_ID/text()').extract())
        Relationships_List_Dict["Relationship"] = dict((k, v) for k, v in Relationship.iteritems() if v)
        Relationships_List.append(dict((k, v) for k, v in Relationships_List_Dict.iteritems() if v)) if dict((k, v) for k, v in Relationships_List_Dict.iteritems() if v ) != {} else None
    return Relationships_List

def Relationship_Notes(self,node):
    Relationship_Notes_List = []
    for relationship_note in node.xpath('Relationship_Note'):
        Relationship_Note = {}
        Relationship_Note["Relationship_Note"] = ",".join([str(i) for i in (structured_text_type(self, relationship_note.xpath('Relationship_Note')))])
        Relationship_Notes_List.append(str(dict((k, v) for k, v in Relationship_Note.iteritems() if v))) if dict((k, v) for k, v in Relationship_Note.iteritems() if v ) != {} else None
    return Relationship_Notes_List

def Weakness_Ordinalities(self,node):
    Weakness_Ordinalities_List = []
    for weakness_ordinality in node.xpath('Weakness_Ordinality'):
        Weakness_Ordinalitie = {}
        Weakness_Ordinalitie["Ordinality"] = "".join(node.xpath('Ordinality/text()').extract())
        Weakness_Ordinalitie["Ordinality_Description"] = ",".join([str(i) for i in structured_text_type(self, node.xpath('Ordinality_Description'))])
        Weakness_Ordinalities_List.append(str(dict((k, v) for k, v in Weakness_Ordinalitie.iteritems() if v))) if dict((k, v) for k, v in Weakness_Ordinalitie.iteritems() if v ) != {} else None
    return Weakness_Ordinalities_List

def Applicable_Platforms(self,node):
    Applicable_Platforms_List = []
    Applicable_Platform_Dict = {}

    for lanquage in node.xpath('Languages'):
        lanquages_Dict = {}
        lanquages_Dict["Language_Name"] = "".join(lanquage.xpath('Language/@Language_Name').extract())
        lanquages_Dict["Prevalence"] = "".join(lanquage.xpath('Language/@Prevalence').extract())
        lanquages_Dict["Language_Class_Description"] = "".join(
            lanquage.xpath('Language_Class/@Language_Class_Description').extract())
        Applicable_Platform_Dict["Languages"] = dict((k, v) for k, v in lanquages_Dict.iteritems() if v)

    Operating_Systems_Dict_All = {}
    for operating_system in node.xpath('Operating_Systems/Operating_System'):
        Operating_Systems_Dict = {}
        Operating_Systems_Dict["Prevalence"] = "".join(operating_system.xpath('@Prevalence').extract())
        Operating_Systems_Dict["Operating_System_Name"] = "".join(operating_system.xpath('@Operating_System_Name').extract())
        Operating_Systems_Dict_All["Operating_System"] = dict((k, v) for k, v in Operating_Systems_Dict.iteritems() if v)
    for operating_system_class in node.xpath('Operating_Systems/Operating_System_Class'):
        Operating_System_Class_Dict={}
        Operating_System_Class_Dict["Prevalence"] = "".join(operating_system_class.xpath('@Prevalence').extract())
        Operating_System_Class_Dict["Operating_System_Class_Description"] = "".join(operating_system_class.xpath('@Operating_System_Class_Description').extract())
        Operating_Systems_Dict_All["Operating_System_Class"] = dict((k, v) for k, v in Operating_System_Class_Dict.iteritems() if v)
        Applicable_Platform_Dict["Operating_Systems"] = dict((k, v) for k, v in Operating_Systems_Dict_All.iteritems() if v)

    Hardware_Architectures = {}
    for hardware_architecture in node.xpath('Hardware_Architectures/Hardware_Architecture'):
        Ha1 = {}
        Ha1["Hardware_Architecture_Name"] = "".join(hardware_architecture.xpath('@Hardware_Architecture_Name').extract())
        Ha1["Prevalence"] = "".join(hardware_architecture.xpath('@Prevalence').extract())
        Hardware_Architectures["Hardware_Architecture"] = dict((k, v) for k, v in Ha1.iteritems() if v)
    for hardware_architecture_class in node.xpath('Hardware_Architectures/Hardware_Architecture_Class'):
        Ha2 = {}
        Ha2["Hardware_Architecture_Class_Name"] = "".join(hardware_architecture_class.xpath('@Hardware_Architecture_Class_Name').extract())
        Ha2["Prevalence"] = "".join(hardware_architecture_class.xpath('@Prevalence').extract())
        Hardware_Architectures["Hardware_Architecture_Class"] = dict((k, v) for k, v in Ha2.iteritems() if v)
        Applicable_Platform_Dict["Hardware_Architectures"] = dict((k, v) for k, v in Hardware_Architectures.iteritems() if v)

    Architectural_Paradigms = {}
    for architectural_paradigm in node.xpath('Architectural_Paradigms'):
        Architectural_Paradigms_Dict = {}
        Architectural_Paradigms_Dict["Architectural_Paradigm_Name"] = "".join(architectural_paradigm.xpath('Architectural_Paradigm/@Architectural_Paradigm_Name').extract())
        Architectural_Paradigms_Dict["Prevalence"] = "".join(architectural_paradigm.xpath('Architectural_Paradigm/@Prevalence').extract())
        Architectural_Paradigms["Architectural_Paradigm"] = dict((k, v) for k, v in Architectural_Paradigms_Dict.iteritems() if v)
        Applicable_Platform_Dict["Architectural_Paradigms"] = dict((k, v) for k, v in Architectural_Paradigms.iteritems() if v)

    Environments = {}
    for environment in node.xpath('Environments'):
        Environments_Dict = {}
        Environments_Dict["Environment_Name"] = "".join(environment.xpath('Environment/@Environment_Name').extract())
        Environments_Dict["Prevalence"] = "".join(environment.xpath('Environment/@Prevalence').extract())
        Environments["Environment"] = dict((k, v) for k, v in Environments_Dict.iteritems() if v)
        Applicable_Platform_Dict["Environments"] = dict((k, v) for k, v in Environments.iteritems() if v)

    Technology_Classes = {}
    for technology_class in node.xpath('Technology_Classes'):
        Technology_Classes_Dict = {}
        Technology_Classes_Dict["Technology_Name"] = "".join(technology_class.xpath('Technology_Class/@Technology_Name').extract())
        Technology_Classes_Dict["Prevalence"] = "".join(technology_class.xpath('Technology_Class/@Prevalence').extract())
        Technology_Classes["Technology_Classe"] = dict((k, v) for k, v in Technology_Classes_Dict.iteritems() if v)
        Applicable_Platform_Dict["Technology_Classes"] = dict((k, v) for k, v in Technology_Classes.iteritems() if v)

    Common_Platform_References = {}
    for common_platform_reference in node.xpath('Common_Platform_References'):
        Common_Platform_References_Dict = {}
        Common_Platform_References_Dict["CPE_ID"] = "".join(common_platform_reference.xpath('Common_Platform_Reference/CPE_ID/text()').extract())
        Common_Platform_References["Common_Platform_Reference"] = dict((k, v) for k, v in Common_Platform_References_Dict.iteritems() if v)
        Applicable_Platform_Dict["Common_Platform_References"] = dict((k, v) for k, v in Common_Platform_References.iteritems() if v)

    Applicable_Platform_Dict["Platform_Notes"] = ",".join([str(i) for i in structured_text_type(self,node.xpath('Platform_Notes'))])
    Applicable_Platforms_List.append(dict((k, v) for k, v in Applicable_Platform_Dict.iteritems() if v)) if dict((k, v) for k, v in Applicable_Platform_Dict.iteritems() if v ) != {} else None

    return Applicable_Platforms_List

def Maintenance_Notes(self, node):
    Maintenance_Notes_List = []
    for maintenance in node:
        Maintenance_Note = {}
        Maintenance_Note["Maintenance_Note"] = ",".join([str(i) for i in structured_text_type(self,maintenance.xpath('Maintenance_Note'))])
        Maintenance_Notes_List.append(dict((k, v) for k, v in Maintenance_Note.iteritems() if v)) if dict((k, v) for k, v in Maintenance_Note.iteritems() if v ) != {} else None
    return Maintenance_Notes_List

def Background_Details(self, node):
    Background_Details_List = []
    for background_detail in node:
        Background_Detail_Dict = {}
        Background_Detail_Dict["Background_Detail"] = ",".join([str(i) for i in structured_text_type(self, background_detail.xpath('Background_Detail'))])
        Background_Details_List.append(dict((k, v) for k, v in Background_Detail_Dict.iteritems() if v)) if dict((k, v) for k, v in Background_Detail_Dict.iteritems() if v ) != {} else None
    return Background_Details_List

def Other_Notes(self, node):
    Other_Notes_List = []
    for other_note in node:
        Other_Notes_Dict = {}
        Other_Notes_Dict["Note"] = ",".join([str(i) for i in structured_text_type(self,other_note.xpath('Note'))])
        Other_Notes_List.append(dict((k, v) for k, v in Other_Notes_Dict.iteritems() if v)) if dict((k, v) for k, v in Other_Notes_Dict.iteritems() if v ) != {} else None
    return Other_Notes_List

def Alternate_Terms(self, node):
    Alternate_Terms_List = []
    Alternate_Terms_Dict_All = {}
    for alternate_term in node.xpath('Alternate_Term'):
        Alternate_Terms_Dict = {}
        Alternate_Terms_Dict["Term"] = "".join(alternate_term.xpath('Term/text()').extract())
        Alternate_Terms_Dict["Alternate_Term_Description"] = ",".join([str(i) for i in structured_text_type(self, alternate_term.xpath('Alternate_Term_Description'))])
        Alternate_Terms_Dict_All["Alternate_Term"] = dict((k, v) for k, v in Alternate_Terms_Dict.iteritems() if v)
        Alternate_Terms_List.append(dict((k, v) for k, v in Alternate_Terms_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Alternate_Terms_Dict_All.iteritems() if v ) != {} else None
    return Alternate_Terms_List

def Terminology_Notes(self, node):
    Terminology_Notes_List = []
    for terminology_note in node:
        Terminology_Notes_Dict = {}
        Terminology_Notes_Dict["Terminology_Note"] = ",".join([str(i) for i in structured_text_type(self, terminology_note.xpath('Terminology_Note'))])
        Terminology_Notes_List.append(str(dict((k, v) for k, v in Terminology_Notes_Dict.iteritems() if v))) if dict((k, v) for k, v in Terminology_Notes_Dict.iteritems() if v ) != {} else None
    return Terminology_Notes_List

def Time_of_Introduction(self, node):
    Time_of_Introduction_List = []
    Time_of_Introduction_Dict_All = {}
    for time_of_introduction in node.xpath('Introductory_Phase'):
        Time_of_Introduction_Dict = {}
        Time_of_Introduction_Dict["Introductory_Phase"] = "".join(time_of_introduction.xpath('text()').extract())
        Time_of_Introduction_Dict_All["Introductory_Phase"] = dict((k, v) for k, v in Time_of_Introduction_Dict.iteritems() if v)
        Time_of_Introduction_List.append(dict((k, v) for k, v in Time_of_Introduction_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Time_of_Introduction_Dict_All.iteritems() if v ) != {} else None
    return Time_of_Introduction_List

def Modes_of_Introduction(self, node):
    Modes_of_Introduction_List = []
    for modes_of_introduction in node:
        Mode_of_Introduction_Dict = {}
        Mode_of_Introduction_Dict["Mode_of_Introduction"] = ",".join([str(i) for i in structured_text_type(self, modes_of_introduction.xpath('Mode_of_Introduction'))])
        Modes_of_Introduction_List.append(str(dict((k, v) for k, v in Mode_of_Introduction_Dict.iteritems() if v))) if dict((k, v) for k, v in Mode_of_Introduction_Dict.iteritems() if v ) != {} else None
    return Modes_of_Introduction_List

def Enabling_Factors_for_Exploitation(self, node):
    Enabling_Factors_for_Exploitation_List = []
    for enabling_factors_for_exploitation in node:
        enabling_factors_for_exploitation_Dict = {}
        enabling_factors_for_exploitation_Dict["Enabling_Factor_for_Exploitation"] = ",".join([str(i) for i in structured_text_type(self, enabling_factors_for_exploitation.xpath('Enabling_Factor_for_Exploitation'))])
        Enabling_Factors_for_Exploitation_List.append(str(dict((k, v) for k, v in enabling_factors_for_exploitation_Dict.iteritems() if v))) if dict((k, v) for k, v in enabling_factors_for_exploitation_Dict.iteritems() if v ) != {} else None
    return Enabling_Factors_for_Exploitation_List

def Likelihood_of_Exploit(self, node):
    Likelihood_of_Exploit_List = []
    Likelihood_of_Exploit_List.append("".join([s for s in node.xpath('text()').extract()]))
    return Likelihood_of_Exploit_List

def Common_Consequences(self, node):
    Common_Consequences_List = []
    Common_Consequences_Dict_All = {}
    for common_consequence in node.xpath('Common_Consequence'):
        Common_Consequences_Dict = {}
        Common_Consequences_Dict["Consequence_Scope"] = "".join(common_consequence.xpath('Consequence_Scope/text()').extract())
        Common_Consequences_Dict["Consequence_Technical_Impact"] = "".join(common_consequence.xpath('Consequence_Technical_Impact/text()').extract())
        Common_Consequences_Dict["Consequence_Note"] = ",".join([str(i) for i in structured_text_type(self, common_consequence.xpath('Consequence_Note'))])
        Common_Consequences_Dict["Common_Consequence_ID"] = "".join(common_consequence.xpath('@Common_Consequence_ID').extract())
        Common_Consequences_Dict_All["Common_Consequence"] = dict((k, v) for k, v in Common_Consequences_Dict.iteritems() if v)
        Common_Consequences_List.append(dict((k, v) for k, v in Common_Consequences_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Common_Consequences_Dict_All.iteritems() if v ) != {} else None
    return Common_Consequences_List

def Detection_Methods(self, node):
    Detection_Methods_List = []
    Detection_Methods_Dict_All = {}
    for detection_method in node.xpath('Detection_Method'):
        Detection_Methods_Dict = {}
        Detection_Methods_Dict["Method_Name"] = "".join(detection_method.xpath('Method_Name/text()').extract())
        Detection_Methods_Dict["Method_Description"] = ",".join([str(i) for i in structured_text_type(self, detection_method.xpath('Method_Description'))])
        Detection_Methods_Dict["Method_Effectiveness"] = "".join(detection_method.xpath('Method_Effectiveness/text()').extract())
        Detection_Methods_Dict["Method_Effectiveness_Notes"] = ",".join([str(i) for i in structured_text_type(self, detection_method.xpath('Method_Effectiveness_Notes'))])
        Detection_Methods_Dict["Detection_Method_ID"] = "".join(detection_method.xpath('@Detection_Method_ID').extract())
        Detection_Methods_Dict_All["Detection_Method"] = dict((k, v) for k, v in Detection_Methods_Dict.iteritems() if v)
        Detection_Methods_List.append(dict((k, v) for k, v in Detection_Methods_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Detection_Methods_Dict_All.iteritems() if v ) != {} else None
    return Detection_Methods_List

def Potential_Mitigations(self, node):
    Potential_Mitigations_List = []
    Potential_Mitigations_Dict_All = {}
    for potential_mitigation in node.xpath('Mitigation'):
        Potential_Mitigations_Dict = {}
        Potential_Mitigations_Dict["Mitigation_ID"] = "".join(potential_mitigation.xpath('@Mitigation_ID').extract())
        Potential_Mitigations_Dict["Mitigation_Phase"] = "".join(
            potential_mitigation.xpath('Mitigation_Phase/text()').extract())
        Potential_Mitigations_Dict["Mitigation_Strategy"] = "".join(
            potential_mitigation.xpath('Mitigation_Strategy/text()').extract())
        Potential_Mitigations_Dict["Applicable_Languages"] = "".join(
            potential_mitigation.xpath('Applicable_Languages/text()').extract())
        Potential_Mitigations_Dict["Mitigation_Description"] = ",".join([str(i) for i in structured_text_type(self, potential_mitigation.xpath('Mitigation_Description'))])
        Potential_Mitigations_Dict["Mitigation_Effectiveness"] = "".join(
            potential_mitigation.xpath('Mitigation_Effectiveness/text()').extract())
        Potential_Mitigations_Dict["Mitigation_Effectiveness_Notes"] = ",".join([str(i) for i in structured_text_type(self, potential_mitigation.xpath('Mitigation_Effectiveness_Notes'))])
        Potential_Mitigations_Dict["SubMitigations"] = "".join(potential_mitigation.xpath('SubMitigations/Mitigation/text()').extract())
        Potential_Mitigations_Dict["References"] = "".join(potential_mitigation.xpath('References/text()').extract())
        Potential_Mitigations_Dict_All["Mitigation"] = dict((k, v) for k, v in Potential_Mitigations_Dict.iteritems() if v)
        Potential_Mitigations_List.append(dict((k, v) for k, v in Potential_Mitigations_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Potential_Mitigations_Dict_All.iteritems() if v ) != {} else None
    return Potential_Mitigations_List

def Causal_Nature(self, node):
    Causal_Nature_List = []
    Causal_Nature_List.append("".join([s for s in node.xpath('text()').extract()]))
    return Causal_Nature_List

def Demonstrative_Examples(self, node):
    Demonstrative_Examples_List = []
    Demonstrative_Examples_Dict_All = {}

    for demonstrative_example in node.xpath('Demonstrative_Example'):
        Demonstrative_Example_Dict = {}
        Demonstrative_Example_Dict["Demonstrative_Example_ID"] = "".join(
            demonstrative_example.xpath('@Demonstrative_Example_ID').extract())
        Demonstrative_Example_Dict["Intro_Text"] = "".join(demonstrative_example.xpath('Intro_Text/text()').extract())
        Demonstrative_Example_Dict["Example_Body"] = ",".join([str(i) for i in structured_text_type(self, demonstrative_example.xpath('Example_Body'))])
        Demonstrative_Examples_Dict_All["Demonstrative_Example"] = dict((k, v) for k, v in Demonstrative_Example_Dict.iteritems() if v)

    for demonstrative_example_reference in node.xpath('Demonstrative_Example/Demonstrative_Example_References'):
        Demonstrative_Example_References_Dict = {}
        Demonstrative_Example_References_Dict["Reference_ID"] = "".join(
            demonstrative_example_reference.xpath('@Reference_ID').extract())
        Demonstrative_Example_References_Dict["Local_Reference_ID"] = "".join(
            demonstrative_example_reference.xpath('@Local_Reference_ID').extract())
        Demonstrative_Example_References_Dict["Reference_Author"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Author/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Title"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Title/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Section"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Section/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Edition"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Edition/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Publication"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Publication/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Publisher"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Publisher/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Date"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Date/text()').extract())
        Demonstrative_Example_References_Dict["Reference_PubDate"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_PubDate/text()').extract())
        Demonstrative_Example_References_Dict["Reference_Link"] = "".join(
            demonstrative_example_reference.xpath('Reference/Reference_Link/text()').extract())
        Demonstrative_Examples_Dict_All["Demonstrative_Example_References"] = dict((k, v) for k, v in Demonstrative_Example_References_Dict.iteritems() if v)
        Demonstrative_Examples_List.append(dict((k, v) for k, v in Demonstrative_Examples_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Demonstrative_Examples_Dict_All.iteritems() if v ) != {} else None
    return Demonstrative_Examples_List

def Observed_Examples(self, node):
    Observed_Examples_List = []
    Observed_Examples_Dict_All = {}
    for observed_example in node.xpath('Observed_Example'):
        Detection_Methods_Dict = {}
        Detection_Methods_Dict["Observed_Example_Reference"] = "".join(
            observed_example.xpath('Observed_Example_Reference/text()').extract())
        Detection_Methods_Dict["Observed_Example_Description"] = "".join(
            observed_example.xpath('Observed_Example_Description/text()').extract())
        Detection_Methods_Dict["Observed_Example_Link"] = "".join(
            observed_example.xpath('Observed_Example_Link/text()').extract())
        Observed_Examples_Dict_All["Observed_Example"] = dict((k, v) for k, v in Detection_Methods_Dict.iteritems() if v)
        Observed_Examples_List.append(dict((k, v) for k, v in Observed_Examples_Dict_All.iteritems() if v)) if dict((k, v) for k, v in Observed_Examples_Dict_All.iteritems() if v ) != {} else None
    return Observed_Examples_List

def Theoretical_Notes(self, node):
    Theoretical_Notes_List = []
    for theoretical_note in node.xpath('Theoretical_Note'):
        Theoretical_Notes_Dict = {}
        Theoretical_Notes_Dict["Theoretical_Note"] = ",".join([str(i) for i in structured_text_type(self, theoretical_note.xpath('Theoretical_Note'))])
        Theoretical_Notes_List.append(str(dict((k, v) for k, v in Theoretical_Notes_Dict.iteritems() if v))) if dict((k, v) for k, v in Theoretical_Notes_Dict.iteritems() if v ) != {} else None
    return Theoretical_Notes_List

def Functional_Areas(self, node):
    Functional_Areas_List = []
    for functional_areas in node:
        Functional_Areas_Dict = {}
        Functional_Areas_Dict["Functional_Area"] = "".join(functional_areas.xpath('Functional_Area/text()').extract())
        Functional_Areas_List.append(str(dict((k, v) for k, v in Functional_Areas_Dict.iteritems() if v))) if dict((k, v) for k, v in Functional_Areas_Dict.iteritems() if v ) != {} else None
    return Functional_Areas_List

def Relevant_Properties(self, node):
    Relevant_Properties_List = []
    for relevant_propertie in node.xpath('Relevant_Property'):
        Relevant_Properties_Dict = {}
        Relevant_Properties_Dict["Relevant_Property"] = "".join(relevant_propertie.xpath('text()').extract())
        Relevant_Properties_List.append(str(dict((k, v) for k, v in Relevant_Properties_Dict.iteritems() if v))) if dict((k, v) for k, v in Relevant_Properties_Dict.iteritems() if v ) != {} else None
    return Relevant_Properties_List

def Affected_Resources(self, node):
    Affected_Resources_List = []
    for affected_resource in node.xpath('Affected_Resource'):
        Affected_Resource_Dict = {}
        Affected_Resource_Dict["Relevant_Property"] = "".join(affected_resource.xpath('text()').extract())
        Affected_Resources_List.append(str(dict((k, v) for k, v in Affected_Resource_Dict.iteritems() if v))) if dict((k, v) for k, v in Affected_Resource_Dict.iteritems() if v ) != {} else None
    return Affected_Resources_List

def Research_Gaps(self, node):
    Research_Gaps_List = []
    for research_gap in node:
        Research_Gaps_Dict = {}
        Research_Gaps_Dict["Research_Gap"] = ",".join([str(i) for i in structured_text_type(self, research_gap.xpath('Research_Gap'))])
        Research_Gaps_List.append(str(dict((k, v) for k, v in Research_Gaps_Dict.iteritems() if v))) if dict((k, v) for k, v in Research_Gaps_Dict.iteritems() if v ) != {} else None
    return Research_Gaps_List

def References(self, node):
    References_List = []
    References_List_Dict = {}
    for reference in node.xpath('Reference'):
        Reference = {}
        Reference["Reference_Author"] = "".join(reference.xpath('Reference_Author/text()').extract())
        Reference["Reference_Title"] = "".join(reference.xpath('Reference_Title/text()').extract())
        Reference["Reference_Section"] = "".join(reference.xpath('Reference_Section/text()').extract())
        Reference["Reference_Edition"] = "".join(reference.xpath('Reference_Edition/text()').extract())
        Reference["Reference_Publication"] = "".join(reference.xpath('Reference_Publication/text()').extract())
        Reference["Reference_Publisher"] = "".join(reference.xpath('Reference_Publisher/text()').extract())
        Reference["Reference_Date"] = "".join(reference.xpath('Reference_Date/text()').extract())
        Reference["Reference_PubDate"] = "".join(reference.xpath('Reference_PubDate/text()').extract())
        Reference["Reference_Link"] = "".join(reference.xpath('Reference_Link/text()').extract())
        Reference["Reference_ID"] = "".join(reference.xpath('@Reference_ID').extract())
        Reference["Local_Reference_ID"] = "".join(reference.xpath('@Local_Reference_ID').extract())
        References_List_Dict["Reference"] = dict((k, v) for k, v in Reference.iteritems() if v)
        References_List.append(dict((k, v) for k, v in References_List_Dict.iteritems() if v)) if dict((k, v) for k, v in References_List_Dict.iteritems() if v ) != {} else None
    return References_List

def Taxonomy_Mappings(self, node):
    Taxonomy_Mappings_List = []
    Taxonomy_Mappings_Dict = {}
    for taxonomy_mapping in node.xpath('Taxonomy_Mapping'):
        Taxonomy_Mapping_Dict = {}
        Taxonomy_Mapping_Dict["Mapped_Taxonomy_Name"] = "".join(
            taxonomy_mapping.xpath('@Mapped_Taxonomy_Name').extract())
        Taxonomy_Mapping_Dict["Mapped_Node_Name"] = "".join(taxonomy_mapping.xpath('Mapped_Node_Name/text()').extract())
        Taxonomy_Mapping_Dict["Mapped_Node_ID"] = "".join(taxonomy_mapping.xpath('Mapped_Node_ID/text()').extract())
        Taxonomy_Mapping_Dict["Mapping_Fit"] = "".join(taxonomy_mapping.xpath('Mapping_Fit/text()').extract())
        Taxonomy_Mappings_Dict["Taxonomy_Mapping"] = dict((k, v) for k, v in Taxonomy_Mapping_Dict.iteritems() if v)
        Taxonomy_Mappings_List.append(dict((k, v) for k, v in Taxonomy_Mappings_Dict.iteritems() if v)) if dict((k, v) for k, v in Taxonomy_Mappings_Dict.iteritems() if v ) != {} else None
    return Taxonomy_Mappings_List

def White_Box_Definitions(self, node):
    White_Box_Definitions_List = []
    for white_box_definition in node:
        White_Box_Definitions_Dict = {}
        White_Box_Definitions_Dict["White_Box_Definition"] = ",".join([str(i) for i in structured_text_type(self, white_box_definition.xpath('White_Box_Definition'))])
        White_Box_Definitions_List.append(str(dict((k, v) for k, v in White_Box_Definitions_Dict.iteritems() if v))) if dict((k, v) for k, v in White_Box_Definitions_Dict.iteritems() if v ) != {} else None
    return White_Box_Definitions_List

def Black_Box_Definitions(self, node):
    Black_Box_Definitions_List = []
    for black_box_definition in node:
        black_box_definition_Dict = {}
        black_box_definition_Dict["Black_Box_Definition"] = ",".join([str(i) for i in structured_text_type(self, black_box_definition.xpath('Black_Box_Definition'))])
        Black_Box_Definitions_List.append(str(dict((k, v) for k, v in black_box_definition_Dict.iteritems() if v))) if dict((k, v) for k, v in black_box_definition_Dict.iteritems() if v ) != {} else None
    return Black_Box_Definitions_List

def Related_Attack_Patterns(self, node):
    Related_Attack_Patterns_List = []
    Related_Attack_Patterns_Dict = {}
    for related_attack_pattern in node.xpath('Related_Attack_Pattern'):
        Related_Attack_Patterns_D = {}
        Related_Attack_Patterns_D["CAPEC_Version"] = "".join(related_attack_pattern.xpath('@CAPEC_Version').extract())
        Related_Attack_Patterns_D["CAPEC_ID"] = "".join(related_attack_pattern.xpath('CAPEC_ID/text()').extract())
        Related_Attack_Patterns_Dict["Related_Attack_Pattern"] = dict((k, v) for k, v in Related_Attack_Patterns_D.iteritems() if v)
        Related_Attack_Patterns_List.append(dict((k, v) for k, v in Related_Attack_Patterns_Dict.iteritems() if v)) if dict((k, v) for k, v in Related_Attack_Patterns_Dict.iteritems() if v ) != {} else None
    return Related_Attack_Patterns_List

def Content_History(self, node):
    Content_History_List = []
    Content_History_List_Dict = {}
    for submission in node.xpath('Submission'):
        Submission = {}
        Submission["Submission_Source"] = "".join(submission.xpath('@Submission_Source').extract())
        Submission["Submitter"] = "".join(submission.xpath('Submitter/text()').extract())
        Submission["Submitter_Organization"] = "".join(submission.xpath('Submitter_Organization/text()').extract())
        Submission["Submission_Date"] = "".join(submission.xpath('Submission_Date/text()').extract())
        Submission["Submission_Comment"] = "".join(submission.xpath('Submission_Comment/text()').extract())

        Content_History_List_Dict["Submission"] = dict((k, v) for k, v in Submission.iteritems() if v)

    for contribution in node.xpath('Contribution'):
        Contribution = {}
        Contribution["Contributor"] = "".join(contribution.xpath('@Submission_Source').extract())
        Contribution["Contribution_Organization"] = "".join(
            contribution.xpath('Contribution_Organization/text()').extract())
        Contribution["Contribution_Date"] = "".join(contribution.xpath('Contribution_Date/text()').extract())
        Contribution["Contribution_Comment"] = "".join(contribution.xpath('Contribution_Comment/text()').extract())
        Contribution["Contribution_Mode"] = "".join(contribution.xpath('@Contribution_Mode').extract())
        Content_History_List_Dict["Contribution"] = dict((k, v) for k, v in Contribution.iteritems() if v)

    for modification in node.xpath('Modification'):
        Modification = {}
        Modification["Modifier"] = "".join(modification.xpath('Modifier/text()').extract())
        Modification["Modifier_Organization"] = "".join(modification.xpath('Modifier_Organization/text()').extract())
        Modification["Modification_Date"] = "".join(modification.xpath('Modification_Date/text()').extract())
        Modification["Modification_Comment"] = "".join(modification.xpath('Modification_Comment/text()').extract())
        Modification["Modification_Importance"] = "".join(modification.xpath('@Modification_Importance').extract())
        Modification["Modification_Source"] = "".join(modification.xpath('@Modification_Source').extract())
        Content_History_List_Dict["Modification"] = dict((k, v) for k, v in Modification.iteritems() if v)

    for previous_entry_names in node.xpath('Previous_Entry_Names'):
        Previous_Entry_Name = {}
        Previous_Entry_Name["Previous_Entry_Name"] = "".join(
            previous_entry_names.xpath('Previous_Entry_Name/text()').extract())
        Previous_Entry_Name["Name_Change_Date"] = "".join(
            previous_entry_names.xpath('Previous_Entry_Name/@Name_Change_Date').extract())
        Content_History_List_Dict["Previous_Entry_Names"] = dict((k, v) for k, v in Previous_Entry_Name.iteritems() if v)

    Content_History_List.append(dict((k, v) for k, v in Content_History_List_Dict.iteritems() if v)) if dict((k, v) for k, v in Content_History_List_Dict.iteritems() if v ) != {} else None
    return Content_History_List
