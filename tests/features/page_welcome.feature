@test @welcome
Feature: Welcome Screen

  @C2893
  Scenario: C2893 Verifying "Welcome" Screen elements
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Welcome Screen
    Then element "HSSLogo" is displayed
    And element "WelcomePicture" is displayed
    And text "Welcome." is displayed into the "WelcomeTitle"
    And text "Use this app to manage your appointments, message doctors, view test results, and more." is displayed into the "WelcomeText"
    And element "ContinueButton" is displayed
    And text "Continue to App" is displayed into the "ContinueButton"

  @C771
  Scenario: C771 Validate "Welcome" Screen only displays the first time
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the SignInStandard Screen
    When the user login to the app
    Then it displays the "Welcome" Screen
    When the user resets the app
    Then it displays the "SignInStandard" Screen
    When the user login to the app
    Then it displays the "MyCareGuide" Screen
