@menu
Feature: Menu Page

  @C793 @standard
  Scenario: Verifying "Menu" Screen elements for Full Account
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    Then element "MenuTitle" is displayed

    Then element "GetCareTitle" is displayed
    And text "Schedule with a Specialist You’ve Seen" is displayed into the "ScheduleSpecialistSeenMenu"
    And text "Schedule with a New Specialist" is displayed into the "ScheduleNewSpecialistMenu"
    And text "Get Immediate Care" is displayed into the "GetImmediateCareMenu"
    And text "View Care Team" is displayed into the "ViewCareTeamMenu"

    Then element "CommunicationTitle" is displayed
    And text "Messages" is displayed into the "MessageMenu"
    And text "Send Message" is displayed into the "SendMessageMenu"
    And text "Letters" is displayed into the "LetterMenu"

    #Then element "ResourcesTitle" is displayed
    #And text "Find a Doctor" is displayed into the "FindDoctorMenu"
    #And text "Find a Therapy Provider Near You" is displayed into the "FindTherapyProviderMenu"
    #And text "Search Conditions and Treatments" is displayed into the "SearchConditionMenu"
    #And text "Find a Location" is displayed into the "FindLocationMenu"
    #And text "Health Videos & Articles" is displayed into the "HealthVideosMenu"
    #And text "Patient Stories" is displayed into the "PatientStoriesMenu"
    #And text "Education & Exercise Resources" is displayed into the "EducationAndExerciseMenu"
    #And text "Search Medical Library" is displayed into the "SearchLibraryMenu"
    #And text "Education" is displayed into the "EducationMenu"
    #And text "Share Feedback" is displayed into the "ShareFeedbackMenu"

    Then element "MyRecordTitle" is displayed
    And text "Test Results" is displayed into the "TestResultsMenu"
    And text "Covid-19" is displayed into the "Covid-19Menu"
    And text "Health Reports" is displayed into the "HealthReportsMenu"
    And text "Preventive Care" is displayed into the "PreventiveCareMenu"
    And text "Plan of Care" is displayed into the "PlanOfCareMenu"
    And text "Advance Health Care Planning" is displayed into the "AdvanceHealthCarePlanningMenu"
    And text "Health Summary" is displayed into the "HealthSummaryMenu"
    And text "Document Center" is displayed into the "DocumentCenterMenu"
    And text "Appointments" is displayed into the "AppointmentsMenu"
    And text "Questionnaires" is displayed into the "QuestionnairesMenu"
    And text "Home Exercise Program" is displayed into the "HomeExerciseProgramMenu"
    And text "Medications" is displayed into the "MedicationsMenu"
    And text "Medical and Family History" is displayed into the "MedicalAndFamilyHistoryMenu"
    And text "To-Do" is displayed into the "To-DoMenu"

    Then element "BillingTitle" is displayed
    And text "Billing Summary" is displayed into the "BillingSummaryMenu"

    Then element "InsuranceTitle" is displayed
    And text "Coverage Details" is displayed into the "CoverageDetailsMenu"
    And text "Claims" is displayed into the "ClaimsMenu"
    And text "Referrals" is displayed into the "ReferralsMenu"

    Then element "SharingTitle" is displayed
    And text "Share My Record" is displayed into the "ShareMyRecordMenu"
    And text "Share Everywhere" is displayed into the "ShareEverywhereMenu"
    And text "Link My Accounts" is displayed into the "LinkMyAccountsMenu"

    Then element "AccountSettingsTitle" is displayed
    And text "Personal Information" is displayed into the "PersonalInformationMenu"
    And text "Account Settings" is displayed into the "AccountSettingsMenu"
    # Personalize menu
    And text "Communication Preferences" is displayed into the "CommunicationPreferencesMenu"
    And text "Other Preferences" is displayed into the "OtherPreferencesMenu"
    And text "Privacy Policy" is displayed into the "PrivacyPolicyMenu"

  @C2927 @limited
  Scenario: Verifying "Menu" Screen elements for Limited Account
    Given a user who is in "LIMITED_USER" state
    And a user who is into the Menu Screen
    Then element "MenuTitle" is displayed
    Then text "Menu" is displayed into the "MenuTitle"

    Then element "GetCareTitle" is displayed
    Then text "Schedule with a Specialist You’ve Seen" is displayed into the "ScheduleSpecialistSeenMenu"
    Then text "Schedule with a New Specialist" is displayed into the "ScheduleNewSpecialistMenu"
    Then text "Get Immediate Care" is displayed into the "GetImmediateCareMenu"
    Then text "View Care Team" is displayed into the "ViewCareTeamMenu"

    Then element "CommunicationTitle" is displayed
    Then text "Messages" is displayed into the "MessageMenu"
    Then text "Send Message" is displayed into the "SendMessageMenu"
    Then text "Letters" is displayed into the "LetterMenu"

    #Then element "ResourcesTitle" is displayed
    #Then text "Find a Doctor" is displayed into the "FindDoctorMenu"
    #Then text "Find a Therapy Provider Near You" is displayed into the "FindTherapyProviderMenu"
    #Then text "Search Conditions and Treatments" is displayed into the "SearchConditionMenu"
    #Then text "Find a Location" is displayed into the "FindLocationMenu"
    #Then text "Health Videos & Articles" is displayed into the "HealthVideosMenu"
    #Then text "Patient Stories" is displayed into the "PatientStoriesMenu"
    #Then text "Education & Exercise Resources" is displayed into the "EducationAndExerciseMenu"
    #Then text "Search Medical Library" is displayed into the "SearchLibraryMenu"
    #Then text "Education" is displayed into the "EducationMenu"
    #Then text "Share Feedback" is displayed into the "ShareFeedbackMenu"

    Then element "MyRecordTitle" is displayed
    Then text "Test Results" is displayed into the "TestResultsMenu"
    #Then text "Covid-19" is displayed into the "Covid-19Menu"
    Then text "Health Reports" is displayed into the "HealthReportsMenu"
    #Then text "Preventive Care" is displayed into the "PreventiveCareMenu"
    Then text "Plan of Care" is displayed into the "PlanOfCareMenu"
    Then text "Advance Health Care Planning" is displayed into the "AdvanceHealthCarePlanningMenu"
    Then text "Health Summary" is displayed into the "HealthSummaryMenu"
    Then text "Document Center" is displayed into the "DocumentCenterMenu"
    Then text "Appointments" is displayed into the "AppointmentsMenu"
    Then text "Questionnaires" is displayed into the "QuestionnairesMenu"
    Then text "Home Exercise Program" is displayed into the "HomeExerciseProgramMenu"
    Then text "Medications" is displayed into the "MedicationsMenu"
    Then text "Medical and Family History" is displayed into the "MedicalAndFamilyHistoryMenu"
    Then text "To-Do" is displayed into the "To-DoMenu"

    Then element "BillingTitle" is displayed
    Then text "Billing Summary" is displayed into the "BillingSummaryMenu"

    Then element "InsuranceTitle" is displayed
    Then text "Coverage Details" is displayed into the "CoverageDetailsMenu"
    Then text "Claims" is displayed into the "ClaimsMenu"
    Then text "Referrals" is displayed into the "ReferralsMenu"

    Then element "SharingTitle" is displayed
    Then text "Share My Record" is displayed into the "ShareMyRecordMenu"
    Then text "Share Everywhere" is displayed into the "ShareEverywhereMenu"
    Then text "Link My Accounts" is displayed into the "LinkMyAccountsMenu"

    Then element "AccountSettingsTitle" is displayed
    Then text "Personal Information" is displayed into the "PersonalInformationMenu"
    Then text "Account Settings" is displayed into the "AccountSettingsMenu"
    Then text "Communication Preferences" is displayed into the "CommunicationPreferencesMenu"
    Then text "Other Preferences" is displayed into the "OtherPreferencesMenu"
    Then text "Privacy Policy" is displayed into the "PrivacyPolicyMenu"
