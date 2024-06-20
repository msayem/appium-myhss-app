@test @logged_out
Feature: Logged Out Landing Page

  @C764
  Scenario: C764 Verifying "Logged Out" Screen elements
    Given a user who is into the LoggedOut Screen
    Then element "HSSLogo" is displayed
    And element "LoggedOutGreeting" is displayed
    And text "How can we help you?" is displayed into the "LoggedOutTitle"
    And text "I’m a Patient" is displayed into the "PatientButton"
    And text "My Employer Referred Me" is displayed into the "EmployeeButton"
    And text "Make an Appointment" is displayed into the "AppointmentLink"
    And text "Search Conditions & Treatments" is displayed into the "TreatmentsLink"
    # And text "Get Directions" is displayed into the "DirectionsLink" ## Option disabled
    And text "FAQs & Support" is displayed into the "SupportLink"
    And text "Privacy Policy" is displayed into the "PrivacyPolicyLink"
    And app "buildVersion" is displayed into the "VersionLabel"

  @C765
  Scenario: C765 Verifying "Logged Out" Screen greetings message
    Given a user who is into the LoggedOut Screen
    # 12 am - 11:59 am local time
    Then greeting "Good morning." is displayed into the "LoggedOutGreeting" if device time is within "00:00" and "11:59"
    # 12 pm - 5:59 pm local time
    And greeting "Good afternoon." is displayed into the "LoggedOutGreeting" if device time is within "12:00" and "17:59"
    # 6 pm - 11:59 pm local time
    And greeting "Good evening." is displayed into the "LoggedOutGreeting" if device time is within "18:00" and "23:59"

  @C766
  Scenario: C766 Accessing "Make an Appointment" Screen
    Given a user who is into the LoggedOut Screen
    When the user clicks the "AppointmentLink"
    Then it displays the "MakeAnAppointment" Screen
    And text "Make an Appointment" is displayed into the "AppointmentTitle"

  @C767
  Scenario: C767 Accessing "Conditions and Treatments" Screen
    Given a user who is into the LoggedOut Screen
    When the user clicks the "TreatmentsLink"
    Then it displays the "SearchConditionsAndTreatments" Screen
    And text "Conditions and Treatments Library" is displayed into the "ConditionsTitle"

  @C769
  Scenario: C769 Accessing "FAQs & Support" Screen
    Given a user who is into the LoggedOut Screen
    When the user clicks the "SupportLink"
    Then it displays the "FAQs&Support" Screen
    And text "Are there any questions " is displayed into the "SupportTitle"

  @C770
  Scenario: C770 Accessing "Privacy Policy" Screen
    Given a user who is into the LoggedOut Screen
    When the user clicks the "PrivacyPolicyLink"
    Then it displays the "PrivacyPolicy" Screen
    And text "HSS Website and Applications Privacy Policy" is displayed into the "PolicyTitle"
