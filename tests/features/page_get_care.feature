@test @get_care
Feature: Get Care Screen

  @C783
  Scenario: C783 Verifying the Get Care Screen elements
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the GetCare Screen
    Then element "GetCareTitle" is displayed
    And text "Get Care" is displayed into the "GetCareTitle"
    And element "GetCareText" is displayed
    And text "Explore your options to get the care you need from our team of experts." is displayed into the "GetCareText"
    And element "ScheduleSpecialistSeenLink" is displayed
    And text "Schedule with a Specialist You’ve Seen" is displayed into the "ScheduleSpecialistSeenLink"
    And element "ScheduleNewSpecialistLink" is displayed
    And text "Schedule with a New Specialist" is displayed into the "ScheduleNewSpecialistLink"
    And element "GetImmediateCareLink" is displayed
    And text "Get Immediate Care" is displayed into the "GetImmediateCareLink"

  @C787
  Scenario: C787 Accessing "Schedule Appointment" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the GetCare Screen
    When the user clicks the "ScheduleSpecialistSeenLink"
    Then it displays the "Printing" Screen
    When the user clicks the "GotItButton"
    Then it displays the "ScheduleAppointment" Screen
    And element "ScheduleTitle" is displayed

  @C788
  Scenario: C788 Accessing "Make an Appointment" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the GetCare Screen
    When the user clicks the "ScheduleNewSpecialistLink"
    Then it displays the "MakeAnAppointment" Screen
    And text "Make an Appointment" is displayed into the "AppointmentTitle"

  @C790
  Scenario: C790 Accessing "Get Immediate Care" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the GetCare Screen
    When the user clicks the "GetImmediateCareLink"
    Then it displays the "GetImmediateCare" Screen
    And text "Get Immediate Access to Care" is displayed into the "ImmediateCareTitle"
