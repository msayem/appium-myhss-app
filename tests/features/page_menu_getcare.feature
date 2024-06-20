@menu @get_care
Feature: Menu Screen - Get Care Section

  @C2932
  Scenario: C2932 Accessing "Schedule Appointment" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ScheduleSpecialistSeenMenu" option
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "ScheduleAppointment" Screen
    And element "ScheduleTitle" is displayed

  @C2933
  Scenario: C2933 Accessing "Make an Appointment" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ScheduleNewSpecialistMenu" option
    Then it displays the "MakeAnAppointment" Screen
    And text "Make an Appointment" is displayed into the "AppointmentTitle"

  @C2934
  Scenario: C2934 Accessing "Get Immediate Care" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "GetImmediateCareMenu" option
    Then it displays the "GetImmediateCare" Screen
    And text "Get Immediate Access to Care" is displayed into the "ImmediateCareTitle"

  @C2935
  Scenario: C2935 Accessing "Care Team" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Menu Screen
    When the user clicks the "ViewCareTeamMenu" option
    Then it displays the "CareTeamAndProviders" Screen
    And element "CareTeamAndProvidersTitle" is displayed
