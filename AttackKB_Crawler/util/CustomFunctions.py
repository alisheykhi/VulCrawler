import re

def structured_text_type (self, node):

    Structured_Text_Type_List=[]
    # nameSpace = '{http://capec.mitre.org/capec-2}'
    for eachnode in node:
        Structured_Text_Type_dict = {}
        Structured_Text_Type_dict["Text_Title"] = ",".join([s for s in eachnode.xpath('capec:Text_Title/text()').extract()])
        Structured_Text_Type_dict["Text"] = ",".join([s for s in eachnode.xpath('capec:Text/text()').extract()])
        Structured_Text_Type_dict["Code"] = ",".join([s for s in eachnode.xpath('capec:Code/text()').extract()])
        Structured_Text_Type_dict["Comment"] = ",".join([s for s in eachnode.xpath('capec:Comment/text()').extract()])
        Structured_Text_Type_dict["Code_Example_Language"] = ",".join([s for s in eachnode.xpath('capec:Code_Example_Language/text()').extract()])
        Image_List = []
        for Image in eachnode.xpath('capec:Images/capec:Image'):
            Image_tmp = {}
            Image_tmp["Image_Location"] = ",".join([s for s in Image.xpath('capec:Image_Location/text()').extract()])
            Image_tmp["Image_Title"] = ",".join([s for s in Image.xpath('capec:Image_Title/text()').extract()])
            Image_List.append(dict((k, v) for k, v in Image_tmp.iteritems() if v)) if dict((k, v) for k, v in Image_tmp.iteritems() if v) !={} else None
        Structured_Text_Type_dict['Images'] = Image_List

        Structured_Text_Type_dict['Block_Nature'] = ",".join([s for s in eachnode.xpath('capec:Block/@Block_Nature').extract()])
        Structured_Text_Type_dict["Block"] = ",".join([str(i) for i in structured_text_type(self, eachnode.xpath('capec:Block'))])
        Structured_Text_Type_List.append(dict((k, v) for k, v in Structured_Text_Type_dict.iteritems() if v )) if dict((k, v) for k, v in Structured_Text_Type_dict.iteritems() if v ) != {} else None
    return Structured_Text_Type_List

def relationshiptype(self,node):
    Relationships_list = []
    for relationship_node in node:
        Relationship_tmp = {}

        Relationship_Views_list = []
        for Relationship_Views_node in relationship_node.xpath('capec:Relationship_Views'):
            Relationship_Views_tmp = {}
            Relationship_Views_tmp["Relationship_View_ID"] = ",".join([s for s in Relationship_Views_node.xpath('capec:Relationship_View_ID/text()').extract()])
            Relationship_Views_tmp["Relationship_View_ID_Ordinal"] = ",".join([s for s in Relationship_Views_node.xpath('capec:Relationship_View_ID/@Ordinal').extract()])
            Relationship_Views_list.append(dict((k, v) for k, v in Relationship_Views_tmp.iteritems() if v)) if dict((k, v) for k, v in Relationship_Views_tmp.iteritems() if v ) != {} else None
        Relationship_tmp['Relationship_Views'] = Relationship_Views_list
        Relationship_tmp["Relationship_Chains_ID"] = ",".join([s for s in relationship_node.xpath('capec:Relationship_Chains/capec:Relationship_Chain_ID/text()').extract()])
        Relationship_tmp["Relationship_Target_Form"] = ",".join([s for s in relationship_node.xpath('capec:Relationship_Target_Form/text()').extract()])
        Relationship_tmp["Relationship_Nature"] = ",".join([s for s in relationship_node.xpath('capec:Relationship_Nature/text()').extract()])
        Relationship_tmp["Relationship_Target_ID"] = ",".join([s for s in relationship_node.xpath('capec:Relationship_Target_ID/text()').extract()])
        Relationship_tmp["Relationship_Description"] = ",".join([str(i) for i in structured_text_type(self,relationship_node.xpath('capec:Relationship_Description'))])
        Relationships_list.append(dict((k, v) for k, v in Relationship_tmp.iteritems() if v)) if dict((k, v) for k, v in Relationship_tmp.iteritems() if v ) != {} else None
    return Relationships_list

def reference(self,node):
    References_list = []
    for Ref in node:
        Refdict = {}
        Refdict["Reference_ID"] = ",".join([s for s in Ref.xpath('@Reference_ID').extract()])
        Refdict["Local_Reference_ID"] = ",".join([s for s in Ref.xpath('@Local_Reference_ID').extract()])
        Refdict["Reference_Author"] = ",".join([s for s in Ref.xpath('capec:Reference_Author/text()').extract()])
        Refdict["Reference_Title"] = ",".join([s for s in Ref.xpath('capec:Reference_Title/text()').extract()])
        Refdict["Reference_Section"] = ",".join([s for s in Ref.xpath('capec:Reference_Section/text()').extract()])
        Refdict["Reference_Edition"] = ",".join([s for s in Ref.xpath('capec:Reference_Edition/text()').extract()])
        Refdict["Reference_Publication"] = ",".join([s for s in Ref.xpath('capec:Reference_Publication/text()').extract()])
        Refdict["Reference_Publisher"] = ",".join([s for s in Ref.xpath('capec:Reference_Publisher/text()').extract()])
        Refdict["Reference_PubDate"] = ",".join([s for s in Ref.xpath('capec:Reference_PubDate/text()').extract()])
        Refdict["Reference_Date"] = ",".join([s for s in Ref.xpath('capec:Reference_Date/text()').extract()])
        Refdict["Reference_Link"] = ",".join([s for s in Ref.xpath('capec:Reference_Link/text()').extract()])
        References_list.append(dict((k, v) for k, v in Refdict.iteritems() if v)) if dict((k, v) for k, v in Refdict.iteritems() if v ) != {} else None
    return References_list

def content_history(self,node):
    Content_History_list = []

    Content_History_dict={}
    submissions_list=[]
    for sub in node.xpath('capec:Submissions/capec:Submission'):
        subdict = {}
        subdict["Submission_Source"] = ",".join([s for s in sub.xpath('@Submission_Source').extract()])
        subdict["Submitter"] = ",".join([s for s in sub.xpath('capec:Submitter/text()').extract()])
        subdict["Submitter_Organization"] = ",".join([s for s in sub.xpath('capec:Submitter_Organization/text()').extract()])
        subdict["Submission_Date"] = ",".join([s for s in sub.xpath('capec:Submission_Date/text()').extract()])
        subdict["Submission_Comment"] = ",".join([s for s in sub.xpath('capec:Submission_Comment/text()').extract()])
        submissions_list.append(dict((k, v) for k, v in subdict.iteritems() if v)) if dict((k, v) for k, v in subdict.iteritems() if v ) != {} else None

    Content_History_dict["Submissions"] = submissions_list

    modifications_list=[]
    for mud in node.xpath('capec:Modifications/capec:Modification'):
        muddict = {}
        muddict["Modification_Source"] = ",".join([s for s in mud.xpath('@Modification_Source').extract()])
        muddict["Modification_Importance"] = ",".join([s for s in mud.xpath('@Modification_Importance').extract()])
        muddict["Modifier"] = ",".join([s for s in mud.xpath('capec:Modifier/text()').extract()])
        muddict["Modifier_Organization"] = ",".join([s for s in mud.xpath('capec:Modifier_Organization/text()').extract()])
        muddict["Modification_Date"] = ",".join([s for s in mud.xpath('capec:Modification_Date/text()').extract()])
        muddict["Modification_Comment"] = ",".join([s for s in mud.xpath('capec:Modification_Comment/text()').extract()])
        modifications_list.append(dict((k, v) for k, v in muddict.iteritems() if v)) if dict((k, v) for k, v in muddict.iteritems() if v ) != {} else None

    Content_History_dict["modifications"] = modifications_list


    contributions_list=[]
    for contribution in node.xpath('capec:Contributions/capec:Contribution'):
        Contribution = {}
        Contribution["Contributor"] = ",".join(contribution.xpath('capec:Contributor/text()').extract())
        Contribution["Contribution_Organization"] = ",".join(contribution.xpath('Contribution_Organization/text()').extract())
        Contribution["Contribution_Date"] = ",".join(contribution.xpath('Contribution_Date/text()').extract())
        Contribution["Contribution_Comment"] = ",".join(contribution.xpath('Contribution_Comment/text()').extract())
        Contribution["Contribution_Mode"] = ",".join(contribution.xpath('@Contribution_Mode').extract())
        contributions_list.append(dict((k, v) for k, v in Contribution.iteritems() if v)) if dict((k, v) for k, v in Contribution.iteritems() if v ) != {} else None

    Content_History_dict["contributions"] = contributions_list


    previous_entry_names_list=[]
    for previous_entry_names in node.xpath('capec:Previous_Entry_Names/capec:Previous_Entry_Name'):
        Previous_Entry_Name = {}
        Previous_Entry_Name["Previous_Entry_Name"] = "".join(previous_entry_names.xpath('Previous_Entry_Name/text()').extract())
        Previous_Entry_Name["Name_Change_Date"] = "".join(previous_entry_names.xpath('Previous_Entry_Name/@Name_Change_Date').extract())
        previous_entry_names_list.append(dict((k, v) for k, v in Previous_Entry_Name.iteritems() if v)) if dict((k, v) for k, v in Previous_Entry_Name.iteritems() if v ) != {} else None

    Content_History_dict["previous_entry_names"] = previous_entry_names_list
    Content_History_list.append(dict((k, v) for k, v in Content_History_dict.iteritems() if v)) if dict((k, v) for k, v in Content_History_dict.iteritems() if v ) != {} else None


    return Content_History_list

def related_weakness(self,node):
    Related_Weakness_list = []
    for Related_Weakness_node in node:
        Related_Weakness_tmp = {}
        Related_Weakness_tmp["CWE_ID"] = ",".join([s for s in Related_Weakness_node.xpath('capec:CWE_ID/text()').extract()])
        Related_Weakness_tmp["Weakness_Relationship_Type"] = ",".join([s for s in Related_Weakness_node.xpath('capec:Weakness_Relationship_Type/text()').extract()])
        Related_Weakness_list.append(dict((k, v) for k, v in Related_Weakness_tmp.iteritems() if v)) if dict((k, v) for k, v in Related_Weakness_tmp.iteritems() if v ) != {} else None
    return  Related_Weakness_list

def related_vulnerability(self,node):
    Related_Vulnerability_list = []
    for Related_Vulnerability_node in node:
        Related_Vulnerability_tmp = {}
        Related_Vulnerability_tmp["Vulnerability_ID"] = ",".join([s for s in Related_Vulnerability_node.xpath('capec:Vulnerability_ID/text()').extract()])
        Related_Vulnerability_tmp["Vulnerability_Description"] = ",".join([str(i) for i in structured_text_type(self,Related_Vulnerability_node.xpath('capec:Vulnerability_Description'))])
        Related_Vulnerability_list.append(dict((k, v) for k, v in Related_Vulnerability_tmp.iteritems() if v)) if dict((k, v) for k, v in Related_Vulnerability_tmp.iteritems() if v ) != {} else None

    return  Related_Vulnerability_list

def attacker_skills_or_knowledge_required(self,node):
    Attacker_Skills_or_Knowledge_Required_list = []
    for Attacker_Skills_or_Knowledge_Required_node in node:
        Attacker_Skills_or_Knowledge_Required_tmp = {}
        Attacker_Skills_or_Knowledge_Required_tmp["Skill_or_Knowledge_Level"] = ",".join([s for s in Attacker_Skills_or_Knowledge_Required_node.xpath('capec:Skill_or_Knowledge_Level/text()').extract()])
        Attacker_Skills_or_Knowledge_Required_tmp["Skill_or_Knowledge_Type"] = ",".join([str(i) for i in structured_text_type(self,Attacker_Skills_or_Knowledge_Required_node.xpath('capec:Skill_or_Knowledge_Type'))])
        Attacker_Skills_or_Knowledge_Required_list.append(dict((k, v) for k, v in Attacker_Skills_or_Knowledge_Required_tmp.iteritems() if v)) if dict((k, v) for k, v in Attacker_Skills_or_Knowledge_Required_tmp.iteritems() if v ) != {} else None

    return Attacker_Skills_or_Knowledge_Required_list

def attack_motivation_consequence(self,node):
    Attack_Motivation_Consequence_list = []
    for Attack_Motivation_Consequence_node in node:
        Attack_Motivation_Consequence_tmp = {}
        Attack_Motivation_Consequence_tmp["Consequence_Scope"] = ",".join([s for s in Attack_Motivation_Consequence_node.xpath('capec:Consequence_Scope/text()').extract()])
        Attack_Motivation_Consequence_tmp["Consequence_Technical_Impact"] = ",".join([s for s in Attack_Motivation_Consequence_node.xpath('capec:Consequence_Technical_Impact/text()').extract()])
        Attack_Motivation_Consequence_tmp["Consequence_Note"] = ",".join([str(i) for i in structured_text_type(self,Attack_Motivation_Consequence_node.xpath('capec:Consequence_Note'))])
        Attack_Motivation_Consequence_tmp["Common_Consequence_ID"] = ",".join([s for s in Attack_Motivation_Consequence_node.xpath('@Common_Consequence_ID').extract()])
        Attack_Motivation_Consequence_list.append(dict((k, v) for k, v in Attack_Motivation_Consequence_tmp.iteritems() if v)) if dict((k, v) for k, v in Attack_Motivation_Consequence_tmp.iteritems() if v ) != {} else None

    return Attack_Motivation_Consequence_list

def attack_execution_flow(self, node):
    Attack_Phases_list = []
    for Attack_Phase_node in node.xpath('capec:Attack_Phases/capec:Attack_Phase'):
        Attack_Phase_tmp = {}
        Attack_Phase_tmp["Attach_Phase_ID"] = Attack_Phase_node.xpath('@ID').extract()
        Attack_Phase_tmp["Attach_Phase_Name"] = Attack_Phase_node.xpath('@Name').extract()

        Attack_Step_list = []
        for Attack_Step_node in Attack_Phase_node.xpath('capec:Attack_Steps/capec:Attack_Step'):

            Attack_Step_tmp = {}
            Attack_Step_tmp["Attack_Step_ID"] = Attack_Step_node.xpath('@ID').extract()

            # *************************************************
            Common_Attack_Step_list = []
            for Common_Attack_Step in Attack_Step_node.xpath('capec:Common_Attack_Step'):
                Common_Attack_Step_tmp={}
                Common_Attack_Step_tmp['Pattern_Specific_Overrides']=custom_attack_steptype(self,Common_Attack_Step.xpath('capec:Pattern_Specific_Overrides'))
                Common_Attack_Step_tmp['Common_Attack_Step_ID'] = ",".join([s for s in Common_Attack_Step.xpath('@Common_Attack_Step_ID').extract()])
                Common_Attack_Step_list.append(dict((k, v) for k, v in Common_Attack_Step_tmp.iteritems() if v)) if dict((k, v) for k, v in Common_Attack_Step_tmp.iteritems() if v ) != {} else None
            Attack_Step_tmp["Common_Attack_Step"] = Common_Attack_Step_list
            # *************************************************

            Attack_Step_tmp["Custom_Attack_Step"] = custom_attack_steptype(self,Attack_Step_node.xpath('capec:Custom_Attack_Step'))

            Attack_Step_list.append(dict((k, v) for k, v in Attack_Step_tmp.iteritems() if v)) if dict((k, v) for k, v in Attack_Step_tmp.iteritems() if v ) != {} else None

        Attack_Phase_tmp["Attack_Step"] = Attack_Step_list
        Attack_Phases_list.append(dict((k, v) for k, v in Attack_Phase_tmp.iteritems() if v)) if dict((k, v) for k, v in Attack_Phase_tmp.iteritems() if v ) != {} else None

    return Attack_Phases_list

def custom_attack_steptype (self, node):

    Custom_Attack_Step_list = []
    for Custom_Attack_Step in node:

        Custom_Attack_Step_tmp = {}
        Custom_Attack_Step_tmp["Attack_Step_Title"] = Custom_Attack_Step.xpath('capec:Attack_Step_Title/text()').extract()
        Custom_Attack_Step_tmp["Attack_Step_Description"] = ",".join([str(i) for i in structured_text_type(self, Custom_Attack_Step.xpath('capec:Attack_Step_Description'))])
        Custom_Attack_Step_tmp["Attack_Step_Technique"] = attack_step_technique(self, Custom_Attack_Step.xpath('capec:Attack_Step_Techniques/capec:Attack_Step_Technique'))
        Custom_Attack_Step_tmp["Indicators"] = indicator(self, Custom_Attack_Step.xpath('capec:Indicators/capec:Indicator'))
        Custom_Attack_Step_tmp["Outcomes"] = outcomes(self, Custom_Attack_Step.xpath('capec:Outcomes/capec:Outcome'))
        Custom_Attack_Step_tmp["Security_Controls"] = security_controls(self, Custom_Attack_Step.xpath('capec:Security_Controls/capec:Security_Control'))
        Custom_Attack_Step_tmp["Observables"] = observablestype(self, Custom_Attack_Step.xpath('capec:Observables'))
        Custom_Attack_Step_list.append(dict((k, v) for k, v in Custom_Attack_Step_tmp.iteritems() if v)) if dict((k, v) for k, v in Custom_Attack_Step_tmp.iteritems() if v ) != {} else None


    return Custom_Attack_Step_list

def attack_step_technique(self, node):

    Attack_Step_Techniques_list=[]
    for Attack_Step_Technique_node in node:
        Attack_Step_Techniques_tmp = {}

        Attack_Step_Techniques_tmp["Attack_Step_Technique_ID"] = ",".join([s for s in Attack_Step_Technique_node.xpath('@ID').extract()])

        Attack_Step_Techniques_tmp["Attack_Step_Technique_Description"] = ",".join([str(i) for i in structured_text_type(self, Attack_Step_Technique_node.xpath('capec:Attack_Step_Technique_Description'))])

        Attack_Step_Techniques_tmp["Leveraged_Attack_Pattern_ID"] = ",".join([s for s in Attack_Step_Technique_node.xpath('capec:Leveraged_Attack_Patterns/capec:Leveraged_Attack_Pattern_ID/text()').extract()])

        Attack_Step_Techniques_tmp["Relevant_Attack_Surface_Elements"] = relevant_attack_surface_elementstype(self,Attack_Step_Technique_node.xpath('capec:Relevant_Attack_Surface_Elements'))

        Attack_Step_Techniques_tmp["Observables"] = observablestype(self, Attack_Step_Technique_node.xpath('capec:Observables').extract())

        Attack_Step_Techniques_tmp["Environments"] = ",".join([s for s in Attack_Step_Technique_node.xpath('capec:Environments/text()').extract()])

        Attack_Step_Techniques_list.append(dict((k, v) for k, v in Attack_Step_Techniques_tmp.iteritems() if v)) if dict((k, v) for k, v in Attack_Step_Techniques_tmp.iteritems() if v ) != {} else None


    return Attack_Step_Techniques_list

def indicator(self, node):
    indicator_list=[]
    for indicator_node in node:
        indicator_tmp = {}

        indicator_tmp["ID"] = indicator_node.xpath('@ID').extract()
        indicator_tmp["type"] = indicator_node.xpath('@type').extract()
        indicator_tmp["Indicator_Description"] = ",".join([str(i) for i in structured_text_type(self, indicator_node.xpath('capec:Indicator_Description'))])
        indicator_tmp["Relevant_Attack_Surface_Elements"] = relevant_attack_surface_elementstype(self,indicator_node.xpath('capec:Relevant_Attack_Surface_Elements'))
        indicator_tmp["Environments"] = ",".join([s for s in indicator_node.xpath('capec:Environments/text()').extract()])
        indicator_tmp["Observables"] = observablestype(self, indicator_node.xpath('capec:Observables'))

        indicator_list.append(dict((k, v) for k, v in indicator_tmp.iteritems() if v)) if dict((k, v) for k, v in indicator_tmp.iteritems() if v ) != {} else None

    return indicator_list

def outcomes(self, node):
    Outcome_list=[]
    for Outcome_node in node:
        Outcome_tmp = {}
        Outcome_tmp["ID"] = Outcome_node.xpath('@ID').extract()
        Outcome_tmp["type"] = Outcome_node.xpath('@type').extract()
        Outcome_tmp["Outcome_Description"] = Outcome_node.xpath('capec:Outcome_Description/text()').extract()
        Outcome_tmp["Relevant_Attack_Surface_Elements"] = relevant_attack_surface_elementstype(self,Outcome_node.xpath('capec:Relevant_Attack_Surface_Elements'))
        Outcome_tmp["Observables"] = observablestype(self, Outcome_node.xpath('capec:Observables'))
        Outcome_list.append(dict((k, v) for k, v in Outcome_tmp.iteritems() if v)) if dict((k, v) for k, v in Outcome_tmp.iteritems() if v ) != {} else None
    return Outcome_list

def security_controls(self, node):
    Security_Control_list=[]
    for Security_Control_node in node:
        Security_Control_tmp = {}

        Security_Control_tmp["ID"] = ",".join([s for s in Security_Control_node.xpath('@ID').extract()])

        Security_Control_tmp["type"] = ",".join([s for s in Security_Control_node.xpath('@type').extract()])

        Security_Control_tmp["Security_Control_Description"] = Security_Control_node.xpath('capec:Security_Control_Description/text()').extract()

        Security_Control_tmp["Relevant_Attack_Surface_Elements"] = relevant_attack_surface_elementstype(self, Security_Control_node.xpath('capec:Relevant_Attack_Surface_Elements'))

        Observable_Evidence_list = []
        for Observable_Evidence_node in Security_Control_node.xpath('capec:Observable_Evidence'):
            Observable_Evidence_tmp = {}
            Observable_Evidence_tmp['IfPresent_Observables'] =  observablestype(self, Observable_Evidence_node.xpath('capec:IfPresent_Observable').extract())
            Observable_Evidence_tmp['IfNotPresent_Observables'] =  observablestype(self, Observable_Evidence_node.xpath('capec:IfNotPresent_Observables').extract())
            Observable_Evidence_list.append(dict((k, v) for k, v in Observable_Evidence_tmp.iteritems() if v)) if dict((k, v) for k, v in Observable_Evidence_tmp.iteritems() if v ) != {} else None
        Security_Control_tmp['Observable_Evidence'] = Observable_Evidence_list

        Security_Control_list.append(dict((k, v) for k, v in Security_Control_tmp.iteritems() if v)) if dict((k, v) for k, v in Security_Control_tmp.iteritems() if v ) != {} else None

    return Security_Control_list

def observablestype(self,node):
    Observables_list = []
    for Observables_node in node:
        Observables_tmp = {}
        # Signature
        Signature_list = []
        for Signature_node in Observables_node.xpath('capec:Observable/capec:Signature'):
            Signature_tmp = {}

            Signature_tmp["Location_Sensor"] = ",".join([s for s in Signature_node.xpath('apec:Location-Sensor/text()').extract()])

            Stateful_Measure_list = []
            for Stateful_Measure_node in Signature_node.xpath('capec:Stateful_Measure'):
                Stateful_Measure_tmp = {}

                Stateful_Measure_tmp["Description"] = ",".join([str(i) for i in structured_text_type(self, Stateful_Measure_node.xpath('capec:Description'))])

                Value_Type_list = []
                for Value_Type_node in Stateful_Measure_node.xpath('capec:Value_Type'):
                    Value_Type_tmp = {}
                    Value_Type_tmp["Objective_Value"] = ",".join([s for s in Value_Type_node.xpath('apec:Objective_Value/text()').extract()])
                    Value_Type_tmp["Trend"] = ",".join([s for s in Value_Type_node.xpath('apec:Trend/text()').extract()])

                    Frequency_list = []
                    for Frequency_node in Value_Type_node.xpath('capec:Frequency'):
                        Frequency_tmp = {}

                        Frequency_tmp["Rate"] = ",".join([s for s in Frequency_node.xpath('@Rate').extract()])
                        Frequency_tmp["Units"] = ",".join([s for s in Frequency_node.xpath('@Units').extract()])
                        Frequency_tmp["Scale"] = ",".join([s for s in Frequency_node.xpath('@Scale').extract()])
                        Frequency_list.append(dict((k, v) for k, v in Frequency_tmp.iteritems() if v)) if dict((k, v) for k, v in Frequency_tmp.iteritems() if v ) != {} else None

                    Value_Type_tmp["Frequency"] = Frequency_list

                    Value_Type_list.append(dict((k, v) for k, v in Value_Type_tmp.iteritems() if v)) if dict((k, v) for k, v in Value_Type_tmp.iteritems() if v ) != {} else None

                Stateful_Measure_tmp["Value_Type"] =  Value_Type_list

                Stateful_Measure_tmp["name"] = ",".join([s for s in Stateful_Measure_node.xpath('@name').extract()])

                Stateful_Measure_list.append(dict((k, v) for k, v in Stateful_Measure_tmp.iteritems() if v)) if dict((k, v) for k, v in Stateful_Measure_tmp.iteritems() if v ) != {} else None

            Signature_tmp["Stateful_Measure"] = Stateful_Measure_list

            Event_list = []
            for Event_node in Signature_node.xpath('capec:Event'):
                Event_tmp = {}
                Event_tmp["Description"] =",".join([str(i) for i in structured_text_type(self, Event_node.xpath('capec:Description'))])
                Action_list = []
                for Action_node in Event_node.xpath('capec:Action/capec:Object/value'):
                    Action_tmp = {}
                    Action_tmp["Objective_Value"] = ",".join([s for s in Action_node.xpath('apec:Objective_Value/text()').extract()])
                    Action_tmp["Change"] = ",".join([s for s in Action_node.xpath('apec:Change/text()').extract()])
                    Delta_list = []
                    for Delta_node in Action_node.xpath('capec:Delta'):
                        Delta_tmp = {}
                        Delta_tmp["Trend"] = ",".join([s for s in Delta_node.xpath('apec:Trend/text()').extract()])

                        Frequency_list=[]
                        for Frequency_node in Delta_node.xpath('capec:Frequency'):
                            Frequency_tmp={}
                            Frequency_tmp["Rate"] = ",".join([s for s in Frequency_node.xpath('@Rate').extract()])
                            Frequency_tmp["Units"] = ",".join([s for s in Frequency_node.xpath('@Units').extract()])
                            Frequency_tmp["Scale"] = ",".join([s for s in Frequency_node.xpath('@Scale').extract()])
                            Frequency_list.append(dict((k, v) for k, v in Frequency_tmp.iteritems() if v)) if dict((k, v) for k, v in Frequency_tmp.iteritems() if v ) != {} else None

                        Delta_tmp["Frequency"] =Frequency_list
                        Delta_list.append(dict((k, v) for k, v in Delta_tmp.iteritems() if v)) if dict((k, v) for k, v in Delta_tmp.iteritems() if v ) != {} else None

                    Action_tmp["Delta"] = Delta_list

                    Action_list.append(dict((k, v) for k, v in Action_tmp.iteritems() if v)) if dict((k, v) for k, v in Action_tmp.iteritems() if v ) != {} else None

                Event_tmp["Action"] = Action_list

                Event_tmp["Event_Type"] = ",".join([s for s in Event_node.xpath('@Event_Type').extract()])

                Event_list.aappend(dict((k, v) for k, v in Event_tmp.iteritems() if v)) if dict((k, v) for k, v in Event_tmp.iteritems() if v ) != {} else None

            Signature_tmp["Event"] = Event_list

            Signature_list.append(dict((k, v) for k, v in Signature_tmp.iteritems() if v)) if dict((k, v) for k, v in Signature_tmp.iteritems() if v ) != {} else None

        Observables_tmp["Signature"] = Signature_list

        #Noisiness
        Observables_tmp["Noisiness"] =",".join([s for s in Observables_node.xpath('capec:Observable/capec:Noisiness/text()').extract()])

        #Ease_of_Obfuscation
        Observables_tmp["Ease_of_Obfuscation"] = ",".join([s for s in Observables_node.xpath('capec:Observable/capec:Ease_of_Obfuscation/text()').extract()])

        #Obfuscation_Techniques
        Obfuscation_Techniques_list = []
        for Obfuscation_Techniques_node in Observables_node.xpath('capec:Observable/capec:Obfuscation_Techniques/capec:Obfuscation_Technique'):
            Obfuscation_Techniques_tmp = {}
            Obfuscation_Techniques_tmp["Description"] =",".join([str(i) for i in structured_text_type(self, Obfuscation_Techniques_node.xpath('capec:Description'))])

            Obfuscation_Techniques_tmp["Observables"] = observablestype(self,Obfuscation_Techniques_node.xpath('capec:Observables'))
            Obfuscation_Techniques_list.append(dict((k, v) for k, v in Obfuscation_Techniques_tmp.iteritems() if v)) if dict((k, v) for k, v in Obfuscation_Techniques_tmp.iteritems() if v ) != {} else None

        Observables_tmp["Obfuscation_Techniques"] =Obfuscation_Techniques_list

        Observables_list.append(dict((k, v) for k, v in Observables_tmp.iteritems() if v)) if dict((k, v) for k, v in Observables_tmp.iteritems() if v ) != {} else None


    return Observables_list

def relevant_attack_surface_elementstype(self,node):
    Relevant_Attack_Surface_ElementsType_list = []
    for Relevant_Attack_Surface_ElementsType_node in node:
        Relevant_Attack_Surface_ElementsType_tmp = {}
        Relevant_Attack_Surface_ElementsType_tmp["Relevant_Functional_Service_ID"] = ",".join([s for s in
                                                                                               Relevant_Attack_Surface_ElementsType_node.xpath(
                                                                                                   'capec:Relevant_Functional_Services/capec:Relevant_Functional_Service_ID/text()').extract()])
        Relevant_Attack_Surface_ElementsType_tmp["Relevant_Protocol_ID"] = ",".join([s for s in
                                                                                     Relevant_Attack_Surface_ElementsType_node.xpath(
                                                                                         'capec:Relevant_Protocols/capec:Relevant_Protocol_ID/text()').extract()])

        Relevant_Attack_Surface_ElementsType_tmp["Relevant_Protocol_Header_ID"] = ",".join([s for s in
                                                                                            Relevant_Attack_Surface_ElementsType_node.xpath(
                                                                                         'capec:Relevant_Protocol_Headers/capec:Relevant_Protocol_Header_ID/text()').extract()])

        Relevant_Attack_Surface_ElementsType_tmp["Relevant_Command_Structure_ID"] = ",".join([s for s in
                                                                                     Relevant_Attack_Surface_ElementsType_node.xpath(
                                                                                         'capec:Relevant_Command_Structures/capec:Relevant_Command_Structure_ID/text()').extract()])

        Relevant_Attack_Surface_ElementsType_list.append(dict((k, v) for k, v in Relevant_Attack_Surface_ElementsType_tmp.iteritems() if v)) if dict((k, v) for k, v in Relevant_Attack_Surface_ElementsType_tmp.iteritems() if v ) != {} else None


    return Relevant_Attack_Surface_ElementsType_list

def target_attack_surfacetype(self,node):
    target_attack_surfacetype_list = []

    Target_Attack_SurfaceType_dict={}
    Target_Attack_SurfaceType_dict["Target_Attack_Surface_Description"] = target_attack_surface_descriptiontype(self, node.xpath('capec:Target_Attack_Surface_Description'))

    Common_Attack_Surface_Description_list = []
    for Common_Attack_Surface_Description_node in node.xpath('capec:Common_Attack_Surface_Description'):
        Common_Attack_Surface_Description_tmp = {}
        Common_Attack_Surface_Description_tmp['Relevant_Attack_Surface_Elements'] = relevant_attack_surface_elementstype(self, Common_Attack_Surface_Description_node.xpath('capec:Relevant_Attack_Surface_Elements'))
        Common_Attack_Surface_Description_tmp['Pattern_Specific_Overrides'] = target_attack_surface_descriptiontype(self, Common_Attack_Surface_Description_node.xpath('capec:Pattern_Specific_Overrides'))
        Common_Attack_Surface_Description_list.append(dict((k, v) for k, v in Common_Attack_Surface_Description_tmp.iteritems() if v)) if dict((k, v) for k, v in Common_Attack_Surface_Description_tmp.iteritems() if v ) != {} else None

    Target_Attack_SurfaceType_dict["Common_Attack_Surface_Description"] = Common_Attack_Surface_Description_list

    target_attack_surfacetype_list.append(dict((k, v) for k, v in Target_Attack_SurfaceType_dict.iteritems() if v)) if dict((k, v) for k, v in Target_Attack_SurfaceType_dict.iteritems() if v ) != {} else None


    return target_attack_surfacetype_list

def target_attack_surface_descriptiontype(self,node):
    Target_Attack_Surface_Description_List = []
    for Target_Attack_Surface_Description in node:

        Target_Attack_Surface_Description_tmp = {}

        Target_Attack_Surface_Description_tmp["Targeted_OSI_Layers"] = ",".join([s for s in Target_Attack_Surface_Description.xpath('capec:Targeted_OSI_Layers/capec:Targeted_OSI_Layer/text()').extract()])
        Target_Attack_Surface_Description_tmp["Target_Attack_Surface_Localities"] = ",".join([s for s in Target_Attack_Surface_Description.xpath('capec:Target_Attack_Surface_Localities/capec:Target_Attack_Surface_Locality/text()').extract()])
        Target_Attack_Surface_Description_tmp["Target_Attack_Surface_Types"] = ",".join([s for s in Target_Attack_Surface_Description.xpath('capec:Target_Attack_Surface_Types/capec:Target_Attack_Surface_Type/text()').extract()])

        Target_Functional_Services_List = []
        for Target_Functional_Service in Target_Attack_Surface_Description.xpath('capec:Target_Functional_Services/capec:Target_Functional_Service'):
            Target_Functional_Service_tmp = {}
            Target_Functional_Service_tmp["ID"] = ",".join([s for s in Target_Functional_Service.xpath('@ID').extract()])
            Target_Functional_Service_tmp["Name"] = ",".join([s for s in Target_Functional_Service.xpath('@Name').extract()])

            Protocol_List = []
            for Protocol in Target_Functional_Service.xpath('capec:Protocol'):
                Protocol_tmp = {}
                Protocol_tmp["Protocol_ID"] = ",".join([s for s in Protocol.xpath('@ID').extract()])
                Protocol_tmp["Protocol_Name"] = ",".join([s for s in Protocol.xpath('@Name').extract()])
                Protocol_tmp["Protocol_RFC"] = ",".join([s for s in Protocol.xpath('@RFC').extract()])
                Protocol_tmp["Protocol_Encryption"] = ",".join([s for s in Protocol.xpath('@Encryption').extract()])
                Protocol_tmp["Protocol_Encryption_Type"] = ",".join([s for s in Protocol.xpath('@Encryption_Type').extract()])

                Protocol_Structure_list = []
                for Protocol_Structure in Protocol.xpath('capec:Protocol_Structure/capec:Protocol_Header'):
                    Protocol_Structure_tmp = {}
                    Protocol_Structure_tmp["Protocol_Header_ID"] = ",".join([s for s in Protocol_Structure.xpath('@ID').extract()])
                    Protocol_Structure_tmp["Protocol_Header_Name"] = ",".join([s for s in Protocol_Structure.xpath('@Name').extract()])
                    Protocol_Structure_tmp["Protocol_Header_RFC"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_RFC/text()').extract()])
                    Protocol_Structure_tmp["Protocol_Header_Field_Name"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_Field_Name/text()').extract()])
                    Protocol_Structure_tmp["Protocol_Header_Field_Description"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_Field_Description/text()').extract()])
                    Protocol_Structure_tmp["Protocol_Flag_Description"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_Flag_Description/text()').extract()])
                    Protocol_Structure_tmp["Protocol_Header_Flag_Value"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_Flag_Value/text()').extract()])
                    Protocol_Structure_tmp["Protocol_Header_Operation_Code"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_Operation_Code/text()').extract()])
                    Protocol_Structure_tmp["Protocol_Header_Data"] = ",".join([s for s in Protocol_Structure.xpath('capec:Protocol_Data/text()').extract()])
                    Protocol_Structure_list.append(dict((k, v) for k, v in Protocol_Structure_tmp.iteritems() if v)) if dict((k, v) for k, v in Protocol_Structure_tmp.iteritems() if v ) != {} else None

                Protocol_tmp["Protocol_Structure"] = Protocol_Structure_list

                Command_Structures_list = []
                for Command_Structures in Protocol.xpath('capec:Command_Structures/capec:Command_Structure'):
                    Command_Structures_tmp = {}
                    Command_Structures_tmp["Command_Structure_ID"] = ",".join([s for s in Command_Structures.xpath('@ID').extract()])
                    Command_Structures_tmp["Command_Structure_Name"] = ",".join([s for s in Command_Structures.xpath('@Name').extract()])
                    Command_Structures_tmp["Command_Structure_Description"] = ",".join([s for s in Command_Structures.xpath('capec:Command_Description/text()').extract()])
                    Command_Structures_tmp["Command_Structure_Type"] = ",".join([s for s in Command_Structures.xpath('capec:Command_Type/text()').extract()])
                    Command_Structures_tmp["Command_Structure_Group_Label"] = ",".join([s for s in Command_Structures.xpath('capec:Command_Group_Label/text()').extract()])
                    Command_Structures_list.append(dict((k, v) for k, v in Command_Structures_tmp.iteritems() if v)) if dict((k, v) for k, v in Command_Structures_tmp.iteritems() if v ) != {} else None

                Protocol_tmp["Command_Structures"] = Command_Structures_list

                Related_Protocols_list = []
                for Related_Protocols in Protocol.xpath('capec:Related_Protocols/capec:Related_Protocol'):
                    Related_Protocols_tmp = {}
                    Related_Protocols_tmp["Name"] = ",".join([s for s in Related_Protocols.xpath('@Name').extract()])
                    Related_Protocols_tmp["RFC"] = ",".join([s for s in Related_Protocols.xpath('@RFC').extract()])
                    Related_Protocols_tmp["Relationship_Type"] = ",".join([s for s in Related_Protocols.xpath('capec:Relationship_Type/text()').extract()])
                    Related_Protocols_list.append(dict((k, v) for k, v in Related_Protocols_tmp.iteritems() if v)) if dict((k, v) for k, v in Related_Protocols_tmp.iteritems() if v ) != {} else None

                Protocol_tmp["Related_Protocols"] = Related_Protocols_list

                Protocol_List.append(dict((k, v) for k, v in Protocol_tmp.iteritems() if v)) if dict((k, v) for k, v in Protocol_tmp.iteritems() if v ) != {} else None


            Target_Functional_Service_tmp["Protocol"] = Protocol_List
            Target_Functional_Services_List.append(dict((k, v) for k, v in Target_Functional_Service_tmp.iteritems() if v)) if dict((k, v) for k, v in Target_Functional_Service_tmp.iteritems() if v ) != {} else None


        Target_Attack_Surface_Description_tmp["Target_Functional_Services"] = Target_Functional_Services_List
        Target_Attack_Surface_Description_List.append(dict((k, v) for k, v in Target_Attack_Surface_Description_tmp.iteritems() if v)) if dict((k, v) for k, v in Target_Attack_Surface_Description_tmp.iteritems() if v ) != {} else None


    return Target_Attack_Surface_Description_List