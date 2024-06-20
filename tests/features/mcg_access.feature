@test @mcg_access
Feature: MCG Screen - Access

  @C758 @C2841 @PRE_OP_ONE_CASE
  Scenario: C758 Accessing "MyCareGuide" Screen for Standard User with PRE_OP status with One Case
    Given a user who is in "PRE_OP_ONE_CASE" state
    And a user who is into the MyCareGuide Screen
    Then data "surgeryTitle" is displayed into the "SurgeryTitle"

  @C2894 @AT_THE_HOSPITAL
  Scenario: C2894 Accessing "MyCareGuide" Screen for Standard User with AT_THE_HOSPITAL status
    Given a user who is in "AT_THE_HOSPITAL" state
    And a user who is into the MyCareGuide Screen
    Then data "surgeryTitle" is displayed into the "SurgeryTitle"

  @C2928 @AT_THE_HOSPITAL @BEDSIDE
  Scenario: C2928 Accessing "MyCareGuide" Screen for Standard User with AT_THE_HOSPITAL_BEDSIDE status
    Given a user who is in "AT_THE_HOSPITAL_BEDSIDE" state
    And a user who is into the MyCareGuide Screen
    Then data "surgeryTitle" is displayed into the "SurgeryTitle"

  @C2895 @POST_OP
  Scenario: C2895 Accessing "MyCareGuide" Screen for Standard User with POST_OP status
    Given a user who is in "POST_OP_ACTIVE" state
    And a user who is into the MyCareGuide Screen
    Then data "surgeryTitle" is displayed into the "SurgeryTitle"
