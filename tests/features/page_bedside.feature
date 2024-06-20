@test @bedside
Feature: Bedside Screen

  @C784
  Scenario: C784 Accessing "HospitalStay" Screen
    Given a user who is in "AT_THE_HOSPITAL_BEDSIDE" state
    And a user who is into the SignInStandard Screen
    When the user login to the app
    Then it displays the "Bedside" Screen
    When the user clicks the "OkButton"
    Then it displays the "HospitalStay" Screen

  @C785
  Scenario: C785 Accessing "Bedside" Screen
    Given a user who is in "AT_THE_HOSPITAL_BEDSIDE" state
    And a user who is into the SignInStandard Screen
    When the user login to the app
    Then it displays the "Bedside" Screen

  @C2929
  Scenario: C2929 Validate "Bedside" Screen only displays the first time
    Given a user who is in "AT_THE_HOSPITAL_BEDSIDE" state
    And a user who is into the SignInStandard Screen
    When the user login to the app
    Then it displays the "Bedside" Screen
    When the user clicks the "OkButton"
    Then it displays the "HospitalStay" Screen
    When the user resets the app
    Then it displays the "SignInStandard" Screen
    When the user login to the app
    Then it displays the "HospitalStay" Screen
