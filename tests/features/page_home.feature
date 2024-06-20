@test @home
Feature: Home Screen

  @C777
  Scenario: C777 Accessing "Appointments" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Home Screen
    When the user clicks the "AppointmentsLink"
    Then it displays the "Appointments" Screen
    And element "AppointmentsTitle" is displayed

  @C778
  Scenario: C778 Accessing "Messages" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Home Screen
    When the user clicks the "MessagesLink"
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "MessageCenter" Screen
    And element "MessageCenterTitle" is displayed

  @C779
  Scenario: C779 Accessing "Test Results" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Home Screen
    When the user clicks the "TestResultsLink"
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "Results" Screen
    And element "ResultsTitle" is displayed

  @C780
  Scenario: C780 Accessing "Billing" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Home Screen
    When the user clicks the "BillingLink"
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "Billing" Screen
    And element "BillingTitle" is displayed