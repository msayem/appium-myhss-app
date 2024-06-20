from pytest_bdd import given, when
import src.helpers.Common as Common
import pytest

@given('the app is launched')
def app_launched():
    pytest.page = 'LoggedOut'


@given('a user who is into the LoggedOut Screen')
def logged_out_page(driver):
    Common.validate_page(driver, 'LoggedOut')
    pytest.page = 'LoggedOut'


@given('a user who is into the SignInStandard Screen')
def login_standard_page(driver):
    logged_out_page(driver)
    Common.click_element(driver, 'PatientButton')
    Common.validate_page(driver, 'SignInStandard')
    pytest.page = 'SignInStandard'


def login_process(driver, user_data):
    Common.click_element(driver, 'UsernameLabel')
    Common.fill_input(driver, user_data['userName'], 'UsernameField')

    Common.click_element(driver, 'PasswordLabel')
    Common.fill_input(driver, user_data['password'], 'PasswordField')

    Common.validate_screenshot_by_page(driver, 'SignInButton')
    driver.hide_keyboard(key_name='go')
    # Common.click_element(driver, 'SignInButton')


@when('the user login to the app')
def login_process_page(driver):
    login_process(driver, pytest.user)


@given('a user who is into the Welcome Screen')
def welcome_page(driver):
    login_standard_page(driver)
    login_process(driver, pytest.user)
    Common.validate_page(driver, 'Welcome')
    pytest.page = 'Welcome'


@given('a user who is into the MyCareGuide Screen')
def my_care_guide_page(driver):
    if pytest.user['type'] != 'bedside':
        welcome_page(driver)
        Common.click_element(driver, 'ContinueButton')

    if pytest.user['type'] == 'bedside':
        login_standard_page(driver)
        login_process(driver, pytest.user)
        Common.validate_page(driver, 'Bedside')
        pytest.page = 'Bedside'
        Common.click_element(driver, 'OkButton')

        Common.validate_page(driver, 'HospitalStay')
        pytest.page = 'HospitalStay'
        Common.click_element(driver, 'HomeButton')

    Common.validate_page(driver, 'MyCareGuide')
    pytest.page = 'MyCareGuide'


@given('a user who is into the Home Screen')
def home_page(driver):
    if pytest.user['type'] == 'standard':
        my_care_guide_page(driver)
        driver.switch_to.context(driver.contexts[0])  # Native
        pytest.page = 'NavigationBar'
        Common.click_element(driver, 'HomeButton')
        Common.validate_page(driver, 'Home')
        pytest.page = 'Home'

    elif pytest.user['type'] == 'limited':
        welcome_page(driver)
        Common.click_element(driver, 'ContinueButton')
        Common.validate_page(driver, 'Home')
        pytest.page = 'Home'


@given('a user who is into the GetCare Screen')
def get_care_page(driver):
    my_care_guide_page(driver)
    driver.switch_to.context(driver.contexts[0])  # Native
    pytest.page = 'NavigationBar'
    Common.click_element(driver, 'GetCareButton')
    Common.validate_page(driver, 'GetCare')
    pytest.page = 'GetCare'


@given('a user who is into the Resources Screen')
def resources_page(driver):
    my_care_guide_page(driver)
    driver.switch_to.context(driver.contexts[0])  # Native
    pytest.page = 'NavigationBar'
    Common.click_element(driver, 'ResourcesButton')
    Common.validate_page(driver, 'Resources')
    pytest.page = 'Resources'


@given('a user who is into the Menu Screen')
def menu_page(driver):
    if pytest.user['type'] == 'standard':
        my_care_guide_page(driver)
        driver.switch_to.context(driver.contexts[0])  # Native

    elif pytest.user['type'] == 'limited':
        welcome_page(driver)
        Common.click_element(driver, 'ContinueButton')
        Common.validate_page(driver, 'Home')

    pytest.page = 'NavigationBar'
    Common.click_element(driver, 'MenuButton')
    Common.validate_page(driver, 'Menu')
    pytest.page = 'Menu'


@given('a user who is into the Make an Appointment Screen')
def make_an_appointment_page(driver):
    resources_page(driver)
    Common.click_element(driver, 'FindDoctorLink')
    Common.validate_page(driver, 'MakeAnAppointment')
    pytest.page = 'MakeAnAppointment'


@given('a user who is into the Conditions and Treatments Screen')
def conditions_treatments_page(driver):
    resources_page(driver)
    Common.click_element(driver, 'TreatmentsLink')
    Common.validate_page(driver, 'SearchConditionsAndTreatments')
    pytest.page = 'SearchConditionsAndTreatments'


@given('a user who is into the HSS Location Screen')
def conditions_treatments_page(driver):
    resources_page(driver)
    Common.click_element(driver, 'FindLocationLink')
    Common.validate_page(driver, 'HSSLocation')
    pytest.page = 'HSSLocation'
