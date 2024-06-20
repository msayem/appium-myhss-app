@menu @insurance
Feature: Menu Screen - Insurance Section

  @C2956
  Scenario: C2956 Accessing "Coverage Details" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "CoverageDetailsMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "CoverageDetails" Screen
    And element "CoverageDetailsTitle" is displayed

  @C2957
  Scenario: C2957 Accessing "Claims" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ClaimsMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "Claims" Screen
    And element "ClaimsTitle" is displayed

  @C2958
  Scenario: C2958 Accessing "Referrals" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ReferralsMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "ReferralsCoverage" Screen
    And element "ReferralsCoverageTitle" is displayed
