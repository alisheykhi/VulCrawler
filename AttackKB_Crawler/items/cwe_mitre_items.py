import scrapy

class CWEMitreCategoryItems(scrapy.Item):
    CWE_ID  =  scrapy.Field()
    CWE_Type =  scrapy.Field()
    CWE_Name = scrapy.Field()
    CWE_status = scrapy.Field()
    Description = scrapy.Field()
    Relationships = scrapy.Field()
    Relationship_Notes = scrapy.Field()
    Weakness_Ordinalities = scrapy.Field()
    Applicable_Platforms = scrapy.Field()
    Maintenance_Notes = scrapy.Field()
    Background_Details = scrapy.Field()
    Other_Notes = scrapy.Field()
    Alternate_Terms = scrapy.Field()
    Terminology_Notes = scrapy.Field()
    Time_of_Introduction = scrapy.Field()
    Modes_of_Introduction = scrapy.Field()
    Enabling_Factors_for_Exploitation = scrapy.Field()
    Likelihood_of_Exploit = scrapy.Field()
    Common_Consequences = scrapy.Field()
    Detection_Methods = scrapy.Field()
    Potential_Mitigations = scrapy.Field()
    Causal_Nature = scrapy.Field()
    Demonstrative_Examples = scrapy.Field()
    Observed_Examples = scrapy.Field()
    Theoretical_Notes = scrapy.Field()
    Functional_Areas = scrapy.Field()
    Relevant_Properties = scrapy.Field()
    Affected_Resources = scrapy.Field()
    Research_Gaps = scrapy.Field()
    References = scrapy.Field()
    Taxonomy_Mappings = scrapy.Field()
    White_Box_Definitions = scrapy.Field()
    Black_Box_Definitions = scrapy.Field()
    Related_Attack_Patterns = scrapy.Field()
    Content_History = scrapy.Field()
    callback = scrapy.Field()

class CWEMitreViewItems(scrapy.Item):

    CWE_ID =  scrapy.Field()
    #type = scrapy.Field()
    CWE_Type =  scrapy.Field()
    View_Structure =  scrapy.Field()
    View_Objective =  scrapy.Field()
    CWE_Name =  scrapy.Field()
    CWE_status =  scrapy.Field()
    Relationships = scrapy.Field()
    View_Audience = scrapy.Field()
    Content_History = scrapy.Field()
    Maintenance_Notes = scrapy.Field()
    Other_Notes = scrapy.Field()
    Research_Gaps = scrapy.Field()
    References = scrapy.Field()
    View_Filter = scrapy.Field()
    Relationship_Notes = scrapy.Field()
    Alternate_Terms = scrapy.Field()
    callback = scrapy.Field()

class CWEMitreWeaknessItems(scrapy.Item):
    CWE_ID  =  scrapy.Field()
    CWE_Type =  scrapy.Field()
    CWE_Name = scrapy.Field()
    CWE_status = scrapy.Field()
    Weakness_Abstraction = scrapy.Field()
    Description = scrapy.Field()
    Relationships = scrapy.Field()
    Relationship_Notes = scrapy.Field()
    Weakness_Ordinalities = scrapy.Field()
    Applicable_Platforms = scrapy.Field()
    Maintenance_Notes = scrapy.Field()
    Background_Details = scrapy.Field()
    Other_Notes = scrapy.Field()
    Alternate_Terms = scrapy.Field()
    Terminology_Notes = scrapy.Field()
    Time_of_Introduction = scrapy.Field()
    Modes_of_Introduction = scrapy.Field()
    Enabling_Factors_for_Exploitation = scrapy.Field()
    Likelihood_of_Exploit = scrapy.Field()
    Common_Consequences = scrapy.Field()
    Detection_Methods = scrapy.Field()
    Potential_Mitigations = scrapy.Field()
    Causal_Nature = scrapy.Field()
    Demonstrative_Examples = scrapy.Field()
    Observed_Examples = scrapy.Field()
    Theoretical_Notes = scrapy.Field()
    Functional_Areas = scrapy.Field()
    Relevant_Properties = scrapy.Field()
    Affected_Resources = scrapy.Field()
    Research_Gaps = scrapy.Field()
    References = scrapy.Field()
    Taxonomy_Mappings = scrapy.Field()
    White_Box_Definitions = scrapy.Field()
    Black_Box_Definitions = scrapy.Field()
    Related_Attack_Patterns = scrapy.Field()
    Content_History = scrapy.Field()
    callback = scrapy.Field()

class CWEMitreCompoundElementItems(scrapy.Item):
    CWE_ID  =  scrapy.Field()
    CWE_Type =  scrapy.Field()
    CWE_Name = scrapy.Field()
    CWE_status = scrapy.Field()
    Compound_Element_Abstraction = scrapy.Field()
    Compound_Element_Structure = scrapy.Field()
    Description = scrapy.Field()
    Relationships = scrapy.Field()
    Relationship_Notes = scrapy.Field()
    Weakness_Ordinalities = scrapy.Field()
    Applicable_Platforms = scrapy.Field()
    Maintenance_Notes = scrapy.Field()
    Background_Details = scrapy.Field()
    Other_Notes = scrapy.Field()
    Alternate_Terms = scrapy.Field()
    Terminology_Notes = scrapy.Field()
    Time_of_Introduction = scrapy.Field()
    Modes_of_Introduction = scrapy.Field()
    Enabling_Factors_for_Exploitation = scrapy.Field()
    Likelihood_of_Exploit = scrapy.Field()
    Common_Consequences = scrapy.Field()
    Detection_Methods = scrapy.Field()
    Potential_Mitigations = scrapy.Field()
    Causal_Nature = scrapy.Field()
    Demonstrative_Examples = scrapy.Field()
    Observed_Examples = scrapy.Field()
    Theoretical_Notes = scrapy.Field()
    Functional_Areas = scrapy.Field()
    Relevant_Properties = scrapy.Field()
    Affected_Resources = scrapy.Field()
    Research_Gaps = scrapy.Field()
    References = scrapy.Field()
    Taxonomy_Mappings = scrapy.Field()
    White_Box_Definitions = scrapy.Field()
    Black_Box_Definitions = scrapy.Field()
    Related_Attack_Patterns = scrapy.Field()
    Content_History = scrapy.Field()
    callback = scrapy.Field()
