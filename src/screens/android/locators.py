from appium.webdriver.common.appiumby import AppiumBy

LOCATORS_ANDROID = {
    "LoggedOutLanding": {
        'HSSLogo': {'type': AppiumBy.ID, 'locator': 'HSSLogo'},
        'LoggedOutGreeting': {'type': AppiumBy.ID, 'locator': 'LoggedOutGreeting'},
        'LandingTitle': {'type': AppiumBy.ID, 'locator': 'LoggedOutTitle'},
        'LoggedOutVideo': {'type': AppiumBy.ID, 'locator': 'LoggedOutVideo'},

        'PatientButton': {'type': AppiumBy.ID, 'locator': 'PatientButton'},
        'EmployeeButton': {'type': AppiumBy.ID, 'locator': 'EmployeeButton'},

        'AppointmentLink': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeCell[@name="AppointmentLink"]//XCUIElementTypeStaticText'},
        'TreatmentsLink': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeCell[@name="TreatmentsLink"]//XCUIElementTypeStaticText'},
        'SupportLink': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeCell[@name="SupportLink"]//XCUIElementTypeStaticText'},

        'PrivacyPolicyLink': {'type': AppiumBy.ID, 'locator': 'PrivacyPolicyLink'},
        'VersionLabel': {'type': AppiumBy.ID, 'locator': 'VersionLabel'}
    },

    "SignInStandard": {
        'BackButton': {'type': AppiumBy.ID, 'locator': 'Back'},
        'SignUpLink': {'type': AppiumBy.ID, 'locator': 'SignUpLink'},
        'WelcomeTitle': {'type': AppiumBy.ID, 'locator': 'WelcomeTitle'},

        'UsernameLabel': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeStaticText[@name="MyHSS Username"]'},
        'UsernameField': {'type': AppiumBy.ID, 'locator': 'UsernameField'},
        'UsernameValidation': {'type': AppiumBy.ID, 'locator': 'UsernameValidation'},

        'PasswordLabel': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeStaticText[@name="Password"]'},
        'PasswordField': {'type': AppiumBy.ID, 'locator': 'PasswordField'},
        'PasswordValidation': {'type': AppiumBy.ID, 'locator': 'PasswordValidation'},

        'RememberMeCheckbox': {'type': AppiumBy.ID, 'locator': 'RememberMeCheckbox'},
        'RememberMeText': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeStaticText[@name="Remember me"]'},

        'SignInButton': {'type': AppiumBy.ID, 'locator': 'SignInButton'},
        'ForgotLabel': {'type': AppiumBy.XPATH, 'locator': '//XCUIElementTypeStaticText[@name="Forgot username or password?"]'},

        'PayBillLink': {'type': AppiumBy.ID, 'locator': '//XCUIElementTypeCell[@name="payBillAsGuest"]//XCUIElementTypeStaticText'},
        'SupportLink': {'type': AppiumBy.ID, 'locator': '//XCUIElementTypeCell[@name="contactFAQs"]//XCUIElementTypeStaticText'}
    },

    "WelcomeScreen": {
        'HSSLogo': {'type': AppiumBy.ID, 'locator': 'HSSLogo'},
        'WelcomePicture': {'type': AppiumBy.ID, 'locator': 'WelcomePicture'},

        'WelcomeTitle': {'type': AppiumBy.ID, 'locator': 'WelcomeTitle'},
        'WelcomeText': {'type': AppiumBy.ID, 'locator': 'WelcomeText'},

        'ContinueButton': {'type': AppiumBy.ID, 'locator': 'ContinueButton'},
    },

    "NavigationBar": {
        'HomeButton': {'type': AppiumBy.ID, 'locator': 'HomeButton'},
        'MyCareGuideButton': {'type': AppiumBy.ID, 'locator': 'MyCareGuideButton'},
        'GetCareButton': {'type': AppiumBy.ID, 'locator': 'GetCareButton'},
        'ResourcesButton': {'type': AppiumBy.ID, 'locator': 'ResourcesButton'},
        'MenuButton': {'type': AppiumBy.ID, 'locator': 'MenuButton'},
    },

    "MyCareGuideScreen": {
        'SurgeryTitle': {'type': AppiumBy.XPATH, 'locator': ''},
    },

    "MakeAnAppointmentOnline": {
        'AppointmentTitle': {'type': AppiumBy.XPATH, 'locator': ''},
    },

    "SearchConditionsAndTreatments": {
        'ConditionsTitle': {'type': AppiumBy.XPATH, 'locator': ''},
    },

    "FAQs&Support": {
        'SupportTitle': {'type': AppiumBy.XPATH, 'locator': ''},
    },
}
