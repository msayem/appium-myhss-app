@menu @sharing
Feature: Menu Screen - Sharing Section

  @C2959
  Scenario: C2959 Accessing "Sharing Hub" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ShareMyRecordMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "SharingHub" Screen
    And element "SharingHubTitle" is displayed

  @C2960
  Scenario: C2960 Accessing "Share Everywhere" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ShareEverywhereMenu" option
    Then it displays the "ShareEverywhere" Screen
    And element "ShareEverywherePicture" is displayed

  @C2961
  Scenario: C2961 Accessing "Link My Accounts" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "LinkMyAccountsMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "LinkMyAccounts" Screen
    And element "LinkMyAccountsTitle" is displayed