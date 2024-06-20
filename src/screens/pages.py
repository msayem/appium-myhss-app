from src.screens.ios.locators import LOCATORS_IOS
from src.screens.android.locators import LOCATORS_ANDROID

LOCATORS = {
    "ios": LOCATORS_IOS,
    "android": LOCATORS_ANDROID
}

PAGES = {
    'LoggedOut': {'identifier': 'LoggedOutTitle'},
    'SignInStandard': {'identifier': 'SignInButton'},
    'Welcome': {'identifier': 'WelcomeTitle'},

    'Home': {'identifier': 'HomeGreeting'},
    'MyCareGuide': {'identifier': 'SurgeryTitle'},
    'GetCare': {'identifier': 'GetCareTitle'},
    'Resources': {'identifier': 'ResourcesTitle'},
    'Menu': {'identifier': 'MenuTitle'},

    'Bedside': {'identifier': 'OkButton'},
    'HospitalStay': {'identifier': 'HomeButton'},

    'Printing': {'identifier': 'PrintingTitle'},
    'Appointments': {'identifier': 'AppointmentsTitle'},
    'MessageCenter': {'identifier': 'MessageCenterTitle'},
    'Results': {'identifier': 'ResultsTitle'},
    'Billing': {'identifier': 'BillingTitle'},
    'ScheduleAppointment': {'identifier': 'ScheduleTitle'},
    'GetImmediateCare': {'identifier': 'ImmediateCareTitle'},
    'MakeAnAppointment': {'identifier': 'AppointmentTitle'},
    'SearchConditionsAndTreatments': {'identifier': 'ConditionsTitle'},
    'HSSLocation': {'identifier': 'HSSLocationTitle'},
    'FAQs&Support': {'identifier': 'SupportTitle'},
    'PrivacyPolicy': {'identifier': 'PolicyTitle'},

    'PSS': {'identifier': 'PSSTitle'},
    'Itinerary': {'identifier': 'ItineraryTitle'},
    'PayAsGuest': {'identifier': 'PayAsGuestTitle'},
}
