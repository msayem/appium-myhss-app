@menu @communications
Feature: Menu Screen - Communication Section

  @C1292
  Scenario: C1292 Accessing "Messages" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "MessagesMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "MessageCenter" Screen
    And element "MessageCenterTitle" is displayed

  @C1293
  Scenario: C1293 Accessing "Send Message" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "SendMessageMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "SendMessage" Screen
    And element "SendMessageTitle" is displayed

  @C2936
  Scenario: C2936 Accessing "Letters" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "LetterMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "Letters" Screen
    And element "LettersTitle" is displayed
