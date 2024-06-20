from allure_commons.types import AttachmentType
from appium import webdriver
from src.helpers.AppiumServer import AppiumServer
from src.helpers.BrowserStack import BrowserStack
from src.helpers.TestRail import TestRail
from src.helpers.Logger import Logger

from datetime import datetime
from settings import *

from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options

import configparser
import pytest
import urllib3
import functools
import allure
import time
import sys
import json
import os

# pytest.ini takes priority over other config files, even when empty.
tool = 'PytestAppiumFramework'
environment_file = 'env.ini'
logfile = "output.log"
logger = Logger(logfile, new=True)


# The pytest_add option hook allows you to add custom command-line options to pytest.
def pytest_addoption(parser):
    print("I am parsing custom CLI arguments to PyTest")
    parser.addoption("--ENV", action="store", default="test",
                     help="which environment to run your tests: dev, test, or prod")
    parser.addoption("--HOST", action="store", default="localhost",
                     help="where to run your tests: localhost or browser_stack")
    parser.addoption('--PLATFORM', action='store', default="ios",
                     help="Choose Platform app: ios or android")
    parser.addoption("--PLATFORM_VERSION", action="store", default="16.4",
                     help="Choose Platform version to run your tests")
    parser.addoption('--DEVICE', action='store', default="simulator",
                     help="Choose Device: simulator / real")
    parser.addoption("--BS_USERNAME", action="store", default="None",
                     help="the user name of Browser Stack")
    parser.addoption("--BS_APIKEY", action="store", default="None",
                     help="the api key of Browser Stack")
    parser.addoption("--TESTRAIL", action="store", default="False",
                     help="Choose if you want to send results into Test Rail")
    parser.addoption("--TESTRAIL_KEY", action="store", default="None",
                     help="the api key of Test Rail")

# set up config and global shared variables
# pytest_configure is a useful initialization hook that’s called after the command-line options are parsed,
# allowing you to configure the test environment before tests are executed.
# pytest_configure to read the file and store its contents in the config object.
# command line options and define markers within your test suite
# pytest_configure sets the stage before your tests run.
# use pytest_configure to - access shared global variables,
# pytest_configure doesn’t return anything, but you can use the config object to access
# and modify the Pytest configuration.
# pytest_configure allows you to add these variables to the config object.

def pytest_configure(config):
    print("I am inside pytest_configure() using config object to set custom CLI arguments")
    # TEST CASE
    # To access below config.variables outside this function need request object request.config
    config.feature = ''
    pytest.feature = ''
    config.scenario_name = ''
    config.test_status = ''
    config.error_description = ''
    pytest.error_description = ''

    # CONFIG DRIVER
    # Storing the global value at the pytest level pytest.env
    config.env = pytest.env = config.getoption("--ENV").lower()
    config.host = pytest.host = (config.getoption("--HOST")).lower()

    config.platform = pytest.platform = (config.getoption("--PLATFORM")).lower()
    config.platform_version = (config.getoption("--PLATFORM_VERSION")).lower()
    config.device = (reformat_text(config.getoption("--DEVICE"))).lower()

    # BROWSER STACK
    config.bs_username = config.getoption("--BS_USERNAME")
    print("--BS_USERNAME: ", config.bs_username)
    config.bs_apikey = config.getoption("--BS_APIKEY")
    print("--BS_APIKEY: ", config.bs_apikey)
    config.session_id = None
    config.force_local = BROWSER_STACK.get('forceLocal')
    print("BS ForceLocal: ", config.force_local)

    # TESTRAIL
    config.testrail = config.getoption("--TESTRAIL")
    config.testrail_key = config.getoption("--TESTRAIL_KEY")

    if os.path.exists(environment_file):
        cfg = configparser.ConfigParser()
        cfg.read(environment_file)

        # TESTRAIL
        config.testrail_key = cfg["keys"]["TESTRAIL_KEY"]

        # BROWSER STACK
        config.bs_username = cfg['keys']['BS_USERNAME']
        config.bs_apikey = cfg['keys']['BS_APIKEY']


# Hooks
# Use the request fixture to access the config object.
def pytest_bdd_before_scenario(request, feature, scenario):
    print("\nI am inside pytest_bdd_before_scenario(request, feature, scenario) running before driver(request)")
    sys.stdout = logger
    pytest.feature = feature.name
    request.config.feature = feature.name
    request.config.scenario_name = scenario.name
    request.config.tags = get_tags(request)
    request.config.test_status = "passed"
    request.config.error_description = ''

    print("\nFEATURE:", feature.name)
    print("SCENARIO:", request.config.scenario_name)
    print('TAGS:', request.config.tags)

# Fixtures
# Use the request fixture to access the config object.
# Fixtures in Pytest solve some of the problems of code duplication and boilerplate.
# They help you define reusable setup or teardown code that can be used across multiple tests.
# Instead of duplicating the same setup in every test, a fixture can be defined once and used in multiple tests.
# A fixture can be used to set up preconditions for a test, provide data, or perform a teardown after a test is finished
# They are defined using the @pytest.fixture decorator in Python and can be passed to test functions as arguments.
# Fixtures are methods in Pytest that provide a fixed baseline for tests to run on top of.
# Fixtures are a potential and common use of conftest.py. The fixtures that you will define will be shared
# among all tests in your test suite. However, defining fixtures in the root conftest.py
# might be useless and it would slow down testing if such fixtures are not used by all tests.


@pytest.fixture()
def driver(request):
    platform_version = None
    print("\nI am inside driver(request) to create appium driver")
    env = request.config.env
    host = request.config.host
    platform = request.config.platform
    if pytest.host == "localhost":
        if request.config.device == 'simulator':
            platform_version = IOS_SIMULATOR.get('platformVersion')
        else:
            platform_version = request.config.platform_version
    elif pytest.host == "browser_stack":
        platform_version = request.config.platform_version
    #pytest.platform_version = IOS_SIMULATOR.get('platformVersion')
    device = request.config.device
    driver = None
    options = None
    capabilities = None

    print('\nENV:', env)
    print('HOST:', host)
    print('DEVICE:', device)
    print('Platform:', platform)
    print('Platform Version:', platform_version)

    if host == "browser_stack":
        urllib3.disable_warnings()
        assert request.config.bs_username != "None", "Add the variable BS_USERNAME in the command line"
        assert request.config.bs_apikey != "None", "Add the variable BS_APIKEY in the command line"

        bs_app = None
        if platform == 'ios':
            bs_app = BROWSER_STACK[env]['iOSApp']
            pytest.bs_app_build_version = f'{BROWSER_STACK[env]["iOSBuildVersion"]} ({env.upper()})'
        elif platform == 'android':
            bs_app = BROWSER_STACK[env]['androidApp']
            pytest.bs_app_build_version = f'{BROWSER_STACK[env]["androidBuildVersion"]} ({env.upper()})'

        remote_caps = {
            # Set build application under test
            "app": bs_app,
            # Specify device and os_version for testing
            "platformName": platform,
            "platformVersion": platform_version,
            "deviceName": device,
            'autoAcceptAlerts': True,
            # Set other BrowserStack capabilities
            'bstack:options': {
                "appiumVersion": BROWSER_STACK.get('appiumVersion'),
                "projectName": BROWSER_STACK.get('projectName'),
                "buildName": pytest.bs_app_build_version,
                "sessionName": request.config.scenario_name,
                "local": request.config.force_local
            },
        }
        if platform == 'ios':
            options = XCUITestOptions().load_capabilities(remote_caps)
        elif platform == 'android':
            options = UiAutomator2Options().load_capabilities(remote_caps)

        print("CAPABILITIES:", json.dumps(remote_caps, indent=4))

        if request.config.force_local:
            BrowserStack(request.config.bs_username, request.config.bs_apikey).start_local()

        credentials = request.config.bs_username + ":" + request.config.bs_apikey
        url = "http://" + credentials + "@hub.browserstack.com:80/wd/hub"
        driver = webdriver.Remote(command_executor=url, options=options)
        # store session driver id
        request.config.session_id = pytest.session_id = driver.session_id
        print("Session ID is", driver.session_id)

        request.config.version_tr = f"{tool} ({host}, {request.config.platform_version}, {request.config.device})"
        print(f'request.config.version_tr:  {request.config.version_tr}')

    if host == "localhost":

        if platform == 'ios':

            if device == 'simulator':
                capabilities = {
                    "platformName": 'iOS',
                    "appium:options": {
                        'automationName': 'XCUITest',
                        'platformVersion': IOS_SIMULATOR.get('platformVersion'),
                        'deviceName': IOS_SIMULATOR.get('device'),
                        'app': f'{os.popen("pwd").read().rstrip()}/apps/ios/{IOS_SIMULATOR[env]["app"]}',
                        'autoAcceptAlerts': True,
                        # 'unicodeKeyboard': False,
                        # 'resetKeyboard': False,
                    }
                }

            elif device == 'real':
                capabilities = {
                    "platformName": 'iOS',
                    "appium:options": {
                        'udid': IOS_REAL['udid'],
                        'automationName': 'XCUITest',
                        # os.popen(cmd) returns an object IO object and read will convert it to str.
                        'app': f'{os.popen("pwd").read().rstrip()}/apps/ios/{IOS_REAL[env]["app"]}',
                        'wdaLaunchTimeout': '90000',
                        'autoAcceptAlerts': True,
                    }
                }

            options = XCUITestOptions().load_capabilities(capabilities)

        elif platform == 'android':

            if device == 'simulator':
                capabilities = {
                    "platformName": 'Android',
                    "appium:options": {
                        'automationName': 'UiAutomator2',
                        'platformVersion': ANDROID_EMULATOR.get('platformVersion'),
                        'deviceName': ANDROID_EMULATOR.get('deviceName'),
                        'app': f'{os.popen("pwd").read().rstrip()}/apps/android/{ANDROID_EMULATOR.get("app")}',
                        'autoGrantPermissions': True,
                        'fullReset': True,
                        # 'allowTestPackages': True
                        # 'appActivity': 'edu.hss.myhss.activities.SplashActivity' }
                    }
                }
            elif device == 'real':
                capabilities = {
                    "platformName": 'Android',
                    "appium:options": {
                        'automationName': 'UiAutomator2',
                        'platformVersion': ANDROID_REAL.get('platformVersion'),
                        'deviceName': ANDROID_REAL.get('deviceName'),
                        'app': f'{os.popen("pwd").read().rstrip()}/apps/ios/{ANDROID_REAL[env]["app"]}',
                        'wdaLaunchTimeout': '90000',
                        'autoAcceptAlerts': True,
                    }
                }
            options = UiAutomator2Options().load_capabilities(capabilities)

        print("CAPABILITIES:", json.dumps(capabilities, indent=4))
        # Start Appium server only locally
        if APPIUM_SERVER is True:
            AppiumServer().start_server()

        # Create and Start driver
        request.config.version_tr = f"{tool} ({host}, {request.config.platform_version}, {request.config.device})"
        print(f'Test Info: {request.config.version_tr}\n')
        # driver = webdriver.Remote(command_executor=url, options=options)
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

    # Execute scenario steps
    yield driver

    # Quit driver and last evidence and logs
    tear_down(request, driver)


# Hooks
# Called when step function failed to execute
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print('I am inside  pytest_bdd_step_error(request, feature, scenario, step, exception)')
    print('\n*** FAILED BLOCK ***')
    pytest.error_description = exception
    request.config.error_description = exception
    request.config.test_status = "failed"

    print(f'FEATURE: {feature.name}')
    print(f'SCENARIO: {scenario.name}')
    print(f'STEP: {step}')
    print(f'STEP Function: {step_func}')
    print(f'STEP Function Args: {step_func_args}')
    print(f'ERROR: {pytest.error_description}')

''' Called after scenario is executed (even if one of steps has failed) '''
def pytest_bdd_after_scenario(request):
    print('\nI am inside pytest_bdd_after_scenario(request)')
    print('TEST STATUS:', request.config.test_status)
    print(f'ERROR: {pytest.error_description}')

    if str(request.config.host).lower() == "browser_stack" and request.config.session_id is not None:
        # endpoint 'app' for mobile app, 'web' for web app
        endpoint = 'app'
        BrowserStack(request.config.bs_username, request.config.bs_apikey).update_test_status(
            endpoint, pytest.session_id, request.config.test_status, str(pytest.error_description))
        video_url = BrowserStack(request.config.bs_username, request.config.bs_apikey).get_video_url(
            request.config.session_id)
        video_allure_attach(video_url)

    # Create a property file
    # f = open("allure-data/environment.properties", "w")
    # f.write(f"Stand={pytest.env}")
    # f.close()


def tear_down(request, driver):
    print("\nI am inside tear_down(request, driver) after test ran")
    screenshot_path = take_screenshot(request, driver)
    print('\nSCREENSHOT NAME:', screenshot_path)

    if request.config.testrail != 'False':
        TestRail(request.config.testrail_key).add_result_for_case(
            request.config.test_status, request.config.error_description, request.config.tags,
            screenshot_path, request.config.version_tr)
    else:
        print("\n*** TEST RAIL ***", request.config.testrail)

    driver.quit()

    if request.config.host == "browser_stack" and request.config.force_local:
        BrowserStack(request.config.bs_username, request.config.bs_apikey).stop_local()
        # BrowserStack.stop_local()

    # Stop Appium server only locally
    if pytest.host == "localhost" and APPIUM_SERVER is True:
        AppiumServer().stop_server()

    # allure attachment
    logger.close()

    # attach log file as TEXT
    allure.attach.file(logfile, 'Log', allure.attachment_type.TEXT)


def get_tags(request):
    markers = request.node.own_markers
    print('Markers: ', markers)
    tags = []
    # range 0 to length-1
    for i in range(len(markers)):
        tags.append(markers[i].name)
    print("Tags: ", tags)
    tags.remove('usefixtures')

    # add Test run id into tags list
    if request.config.testrail != 'False':
        tags.append(request.config.testrail)
        print("Tags with testRail: ", tags)

    return tags


def get_status(request, failed_before):
    test_status = 'failed' if request.session.testsfailed != failed_before else 'passed'
    return test_status


def take_screenshot(request, driver):
    # create screenshots folder if doesn't exist
    print('\n I am inside take_screenshot(request, driver) called from tear_down(request, driver):')
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # clean the test_name
    list_to_replace = [(' ', '_'), ("'", ''), ('"', ''), ('-', ''), (':', ''), ('/', '_')]
    screenshot_name = functools.reduce(lambda a, kv: a.replace(*kv), list_to_replace, request.config.scenario_name)
    now = datetime.now().strftime('%Y_%m_%d_%H%M%S')
    print('Time: ', now)

    filename = f"screenshots/{screenshot_name}_{now}.png"
   # print('\nSCREENSHOT NAME:', filename)
    time.sleep(1)
    # driver.save_screenshot(filename)
    attachment_png = driver.get_screenshot_as_png()
    '''open for writing binary mode for attaching screenshot in TestRail test run'''
    with open(filename, "wb") as f:
        f.write(attachment_png)

    # allure attachment
    # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    allure.attach(attachment_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    return filename


def video_allure_attach(video_url):
    # attach video as HTML
    allure.attach(
        f'<iframe src="{video_url}" width="100%" height="200" allowfullscreen="allowfullscreen"></iframe>',
        'Video', allure.attachment_type.HTML)


def reformat_text(text):
    list_to_replace = ('_', ' '), ("'", '')
    new_text = functools.reduce(lambda a, kv: a.replace(*kv), list_to_replace, text)
    return new_text
