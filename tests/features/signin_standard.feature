@test @sign_in
Feature: Sign In - Standard user

  @C2920
  Scenario: C2920 Verifying "Sign In Standard" Screen elements
    Given a user who is into the SignInStandard Screen
    # Then text "Welcome to HSS" is displayed into the "SignInTitle"
    Then element "BackButton" is displayed
    And element "SignUpLink" is displayed
    And element "UsernameLabel" is displayed
    And element "PasswordLabel" is displayed
    And element "RememberMeCheckbox" is displayed
    # And text "Remember me" is displayed into the "RememberMeText"
    And element "SignInButton" is displayed
    And element "ForgotLabel" is displayed
    # And element "ForgotUsernameLink" is displayed
    # And element "ForgotPasswordLink" is displayed
    And element "PayBillLink" is displayed
    And element "SupportLink" is displayed

  @C855
  Scenario: C855 Success "required" message displayed for username
    Given a user who is into the SignInStandard Screen
    When the user clicks the "UsernameLabel"
    And the user clicks the "PasswordLabel"
    Then text "Please enter your username" is displayed into the "UsernameValidation"

  @C1099
  Scenario: C1099 Success "required" message displayed for password
    Given a user who is into the SignInStandard Screen
    When the user clicks the "PasswordLabel"
    And the user clicks the "UsernameLabel"
    Then text "Please enter your password" is displayed into the "PasswordValidation"

  @C759
  Scenario: C759 Error message displayed for incorrect Standard User credentials
    Given a user who is in "ACTIVE" state
    And a user who is into the SignInStandard Screen
    When the user clicks the "UsernameLabel"
    # valid username
    And the user fills data "userName" in the "UsernameField"
    And the user clicks the "PasswordLabel"
    # invalid password
    And the user fills "InvalidPassword" in the "PasswordField"
    # And the user clicks the "SignInButton"
    And the user clicks the "go" key in virtual keyboard
    Then text "The username and password don’t match." is displayed into the "PasswordValidation"

  @C2921
  Scenario: C2921 Verifying accessing "Pay as Guest" Screen elements
    Given a user who is into the SignInStandard Screen
    When the user clicks the "PayBillLink"
    Then it displays the "PayAsGuest" Screen
    And text "Pay as Guest" is displayed into the "PayAsGuestTitle"

  @C2922
  Scenario: C2922 Verifying accessing "FAQs & Support" Screen elements
    Given a user who is into the SignInStandard Screen
    When the user clicks the "SupportLink"
    Then it displays the "FAQs&Support" Screen
    And text "Are there any questions " is displayed into the "SupportTitle"

