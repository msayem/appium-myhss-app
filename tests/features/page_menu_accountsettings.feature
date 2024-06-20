@menu @account_settings
Feature: Menu Screen - Account Settings Section

  @C2962
  Scenario: C2962 Accessing "Personal Information" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "PersonalInformationMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "PersonalInformation" Screen
    And element "PersonalInformationTitle" is displayed

  @C2963
  Scenario: C2963 Accessing "Account Settings" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "AccountSettingsMenu" option
    Then it displays the "AccountSettings" Screen
    And element "AccountSettingsTitle" is displayed

  @C2964
  Scenario: C2964 Accessing "Personalize" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "PersonalizeMenu" option
    Then it displays the "Personalize" Screen
    And element "PersonalizeTitle" is displayed

  @C2965
  Scenario: C2965 Accessing "Communication Preferences" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "CommunicationPreferencesMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "CommunicationPreferences" Screen
    And element "CommunicationPreferencesTitle" is displayed

  @C2966
  Scenario: C2966 Accessing "Other Preferences" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "OtherPreferencesMenu" option
    Then it displays the "OtherPreferences" Screen
    And element "OtherPreferencesTitle" is displayed

  @C2967
  Scenario: C2967 Accessing "Privacy Policy" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "PrivacyPolicyMenu" option
    Then it displays the "PrivacyPolicy" Screen
    And element "PolicyTitle" is displayed

