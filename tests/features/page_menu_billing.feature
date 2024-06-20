@menu @billing
Feature: Menu Screen - Billing Section

  @C2955
  Scenario: C2955 Accessing "Billing Summary" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "BillingSummaryMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "Billing" Screen
    And element "BillingTitle" is displayed