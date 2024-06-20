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

tool = 'PytestAppiumFramework'
environment_file = 'env.ini'
logfile = "output.log"
logger = Logger(logfile, new=True)


def pytest_addoption(parser):
    parser.addoption("--ENV", action="store", default="test",
                     help="which environment to run your tests: dev, test, or prod")
    parser.addoption("--HOST", action="store", default="localhost",
                     help="where to run your tests: localhost or browser_stack")
    parser.addoption('--PLATFORM', action='store', default="ios",
                     help="Choose Platform app: ios or android")
    parser.addoption("--PLATFORM_VERSION", action="store", default="None",
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


# set up config variables
def pytest_configure(config):
    # TEST CASE
    config.feature = ''
    config.scenario_name = ''
    config.test_status = ''
    config.error_description = ''

    # CONFIG DRIVER
    config.env = pytest.env = (config.getoption("--ENV")).lower()
    config.host = pytest.host = (config.getoption("--HOST")).lower()

    config.platform = pytest.platform = (config.getoption("--PLATFORM")).lower()
    config.platform_version = (config.getoption("--PLATFORM_VERSION")).lower()
    config.device = (reformat_text(config.getoption("--DEVICE"))).lower()

    # BROWSER STACK
    config.bs_username = config.getoption("--BS_USERNAME")
    config.bs_apikey = config.getoption("--BS_APIKEY")
    config.session_id = None
    config.force_local = BROWSER_STACK.get('forceLocal')

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
def pytest_bdd_before_scenario(request, feature, scenario):

    sys.stdout = logger

    request.config.feature = feature.name
    request.config.scenario_name = scenario.name
    request.config.tags = get_tags(request)
    request.config.test_status = "passed"
    request.config.error_description = ''

    print("\nFEATURE:", request.config.feature)
    print("SCENARIO:", request.config.scenario_name)
    print('TAGS:', request.config.tags)


# Fixtures
@pytest.fixture()
def driver(request):
    env = request.config.env
    host = request.config.host
    platform = request.config.platform
    platform_version = request.config.platform_version
    device = request.config.device
    driver = None
    options = None
    capabilities = None

    print('\nENV:', env)
    print('HOST:', host)
    print('DEVICE:', device)

    if host == "browser_stack":
        urllib3.disable_warnings()
        assert request.config.bs_username != "None", "Add the variable BS_USERNAME in the command line"
        assert request.config.bs_apikey != "None", "Add the variable BS_APIKEY in the command line"

        bs_app = None
        if platform == 'ios':
            bs_app = BROWSER_STACK[env]['iOSApp']
            pytest.bs_app_build_version = BROWSER_STACK[env]['iOSBuildVersion']
        elif platform == 'android':
            bs_app = BROWSER_STACK[env]['androidApp']
            pytest.bs_app_build_version = BROWSER_STACK[env]['androidBuildVersion']

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
                "projectName": f"{BROWSER_STACK.get('projectName')} - {env.upper()}",
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
        driver = webdriver.Remote(command_executor=url, options=options, direct_connection=True)
        # store session driver id
        request.config.session_id = driver.session_id

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
                        # 'appActivity': 'edu.hss.myhss.activities.SplashActivity'
                    }
                }

            options = UiAutomator2Options().load_capabilities(capabilities)

        print("CAPABILITIES:", json.dumps(capabilities, indent=4))
        # Start Appium server only locally
        if APPIUM_SERVER is True:
            AppiumServer().start_server()

        # Start driver
        request.config.version_tr = f"{tool} ({host}, {request.config.platform_version}, {request.config.device})"
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

    # Execute scenario steps
    yield driver

    # Quit driver and last evidence and logs
    tear_down(request, driver)


def tear_down(request, driver):
    screenshot = take_screenshot(request, driver)
    print('\nSCREENSHOT:', screenshot)

    if request.config.testrail != 'False':
        TestRail(request.config.testrail_key).add_result_for_case(
            request.config.test_status, request.config.error_description, request.config.tags,
            screenshot, request.config.version_tr)
    else:
        print("\n*** TEST RAIL ***", request.config.testrail)

    driver.quit()

    if request.config.host == "browser_stack" and request.config.force_local:
        BrowserStack(request.config.bs_username, request.config.bs_apikey).stop_local()

    # Stop Appium server only locally
    if pytest.host == "localhost" and APPIUM_SERVER is True:
        AppiumServer().stop_server()

    # allure attachment
    logger.close()
    allure.attach.file(logfile, 'Log', allure.attachment_type.TEXT)


def get_tags(request):
    markers = request.node.own_markers
    tags = []
    for i in range(len(markers)):
        tags.append(markers[i].name)
    tags.remove('usefixtures')

    # add Test run id into tags list
    if request.config.testrail != 'False':
        tags.append(request.config.testrail)

    return tags


def get_status(request, failed_before):
    test_status = 'failed' if request.session.testsfailed != failed_before else 'passed'
    return test_status


def take_screenshot(request, driver):
    # create screenshots folder if doesn't exist
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # clean the test_name
    list_to_replace = (' ', '_'), ("'", ''), ('"', ''), ('-', ''), (':', ''), ('/', '_')
    screenshot_name = functools.reduce(lambda a, kv: a.replace(*kv), list_to_replace, request.config.scenario_name)
    now = datetime.now().strftime('%Y_%m_%d_%H%M%S')

    filename = f"screenshots/{screenshot_name}_{now}.png"
    time.sleep(1)
    # driver.save_screenshot(filename)
    attachment_png = driver.get_screenshot_as_png()
    with open(filename, "wb") as f:
        f.write(attachment_png)

    # allure attachment
    allure.attach(attachment_png, name="Screenshot", attachment_type=AttachmentType.PNG)

    return filename


# Hooks
def pytest_bdd_step_error(request, feature, scenario, step, exception):
    print('\n*** FAILED BLOCK ***')
    request.config.error_description = exception
    request.config.test_status = "failed"

    print(f'FEATURE: {feature.name}')
    print(f'SCENARIO: {scenario.name}')
    print(f'STEP: {step}')
    print(f'ERROR: {exception}')


def video_allure_attach(video_url):
    allure.attach(
        f'<iframe src="{video_url}" width="100%" height="200" allowfullscreen="allowfullscreen"></iframe>',
        'Video', allure.attachment_type.HTML)


def pytest_bdd_after_scenario(request):
    print('TEST STATUS:', request.config.test_status)

    if str(request.config.host).lower() == "browser_stack" and request.config.session_id is not None:
        # endpoint 'app' for mobile app, 'web' for web app
        endpoint = 'app'
        BrowserStack(request.config.bs_username, request.config.bs_apikey).update_test_status(
            endpoint, request.config.session_id, request.config.test_status, str(request.config.error_description))
        video_url = BrowserStack(request.config.bs_username, request.config.bs_apikey).get_video_url(request.config.session_id)
        video_allure_attach(video_url)

    # Create a property file
    # f = open("allure-data/environment.properties", "w")
    # f.write(f"Stand={pytest.env}")
    # f.close()


def reformat_text(text):
    list_to_replace = ('_', ' '), ("'", '')
    new_text = functools.reduce(lambda a, kv: a.replace(*kv), list_to_replace, text)
    return new_text
