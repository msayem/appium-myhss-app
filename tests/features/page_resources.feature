@test @resources
Feature: Resources Screen

  @C2923
  Scenario: C2923 Verifying "Resources" Screen elements for Standard User
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Resources Screen
    Then element "ResourcesTitle" is displayed
    And text "Find a Doctor" is displayed into the "FindDoctorLink"
    And text "Search Conditions and Treatments" is displayed into the "TreatmentsLink"
    And text "Find a Location" is displayed into the "FindLocationLink"
    And text "Move Better Feel Better" is displayed into the "MoveBetterLink"
    And text "Patient Stories" is displayed into the "PatientLink"
    And text "Education & Exercise Resources" is displayed into the "EducationExerciseLink"

  @C2924
  Scenario: C2924 Verifying Accessing "Make an Appointment" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Resources Screen
    When the user clicks the "FindDoctorLink"
    Then it displays the "MakeAnAppointment" Screen
    And element "AppointmentTitle" is displayed
    And text "Make an Appointment" is displayed into the "AppointmentTitle"

  @C2925
  Scenario: C2925 Verifying Accessing "Conditions and Treatments" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Resources Screen
    When the user clicks the "TreatmentsLink"
    Then it displays the "SearchConditionsAndTreatments" Screen
    And element "ConditionsTitle" is displayed
    And text "Conditions and Treatments Library" is displayed into the "ConditionsTitle"

  @C2926
  Scenario: C2926 Verifying Accessing "HSS Locations" Screen
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the Resources Screen
    When the user clicks the "FindLocationLink"
    Then it displays the "HSSLocation" Screen
    And element "HSSLocationTitle" is displayed
