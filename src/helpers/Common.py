from src.screens.pages import LOCATORS
from src.screens.pages import PAGES
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

import pytest
import allure
import time

wait_l = 20


def get_locator(key, page_name):
    locator = None
    platform = pytest.platform
    try:
        locator_by = LOCATORS[platform][page_name][key]['by']
        locator_value = LOCATORS[platform][page_name][key]['value']

        locator = (locator_by, locator_value)
        print('Locator:', locator)
    except KeyError:
        assert locator is not None, f'Key "{key}" not found within "{page_name}" in locators file'
    return locator


def scroll_to_get_element_visible1(driver, key, locator):
    try:
        element = get_element_visible(driver, key, locator, wait_scroll=5)
    except Exception as e:
        allure_screenshot(driver)
        print("Scrolling action")
        swipe_up(driver)
        # get the element after scroll
        element = get_element_visible(driver, key, locator, wait_scroll=5)
    return element


def scroll_to_get_element_visible (driver, key, locator, attempts=5):
    element = None
    for i in range(attempts):
        try:
            element = get_element_visible(driver, key, locator, wait_scroll=5)
            break
        except Exception as e:
            swipe_up(driver)
    return element


def swipe_up(driver):
    window_size = driver.get_window_size()
    mid_x, mid_y = window_size['width'] / 2, window_size['height'] / 2
    driver.swipe(mid_x, window_size['height'] - 100, mid_y, 100, 2000)


def get_element_visible(driver, key, locator, wait_scroll=None):
    wait_d = wait_l
    if wait_scroll is not None:
        wait_d = wait_scroll

    element = WebDriverWait(driver, wait_d).until(
        EC.visibility_of_element_located(locator),
        message=f'Element "{pytest.page}.{key}" not found in DOM')
    return element


def get_elements_visible(driver, key, locator):
    elements = WebDriverWait(driver, wait_l).until(
        EC.presence_of_all_elements_located(locator),
        message=f'Elements "{pytest.page}.{key}" not found in DOM')
    return elements


def get_element_clickable(driver, key, locator):
    element = WebDriverWait(driver, wait_l).until(
        EC.element_to_be_clickable(locator),
        message=f'Element "{pytest.page}.{key}" is not clickable')
    return element


def verify_element_text(key, expected_text, element):
    current_text = element.text

    assert current_text == expected_text, \
        f'The element "{pytest.page}.{key}" not contain the expected text: "{expected_text}". ' \
        f'Text found "{current_text}"'


def fill_input(driver, text, key):
    locator = get_locator(key, pytest.page)
    element = get_element_visible(driver, key, locator)
    element.send_keys(text)


def validate_screenshot_by_page(driver, key):
    if key in ['PatientButton', 'SignInButton', 'ContinueButton', 'TaskButton', 'HomeButton', 'OkButton']:
        allure_screenshot(driver)
        print(f"Action: Tapping {pytest.page}.{key}")


def click_element(driver, key):
    validate_screenshot_by_page(driver, key)
    locator = get_locator(key, pytest.page)
    element = get_element_clickable(driver, key, locator)
    element.click()


def validate_page(driver, page_name):
    data_page = PAGES.get(page_name)
    print('Validate data_page from dictionary:',  data_page)
    identifier = data_page['identifier']
    print('Page identifier from dictionary:', identifier)
    locator = get_locator(identifier, page_name)

    # Switch to WEB_VIEW context, only apply for some pages
    if page_name == "MyCareGuide":
        switch_to_webview(driver, expected_context=2, web_view_index=1)
        verify_only_one_window(driver)
        # switch_to_new_window(driver, expected_windows=2, window_index=1)
    if page_name == "HSSLocation":
        switch_to_webview(driver, expected_context=3, web_view_index=2)
   # \ continuing a line of code
    WebDriverWait(driver, wait_l). \
        until(EC.visibility_of_element_located(locator),
              message=f'Element "{page_name}.{identifier}" not found in DOM. Review identifier of the Page')


def switch_to_webview(driver, expected_context, web_view_index):
    found = False
    contexts = None
    # Wait for 10 attempts with a 2-second interval
    for i in range(6):
        # Get the available contexts
        contexts = driver.contexts
        print(f"contexts [{i}]:", contexts)
        # Wait until number of context expected
        if len(contexts) >= expected_context:
            found = True
            break
        time.sleep(2)
    assert found, f'(Expected Page: "{pytest.page}". No new context found)'

    if 'WEBVIEW' in contexts[web_view_index]:
        driver.switch_to.context(contexts[web_view_index])
        print("Switched to web view context:", contexts[web_view_index])
        return True

    raise Exception(f'Expected Page: "{pytest.page}". No web view context found')


def verify_only_one_window(driver):
    window_handles = None
    # Wait for 5 attempts with a 1-second interval
    for i in range(5):
        # Get the available windows
        window_handles = driver.window_handles
        print(f"Windows [{i}]:", window_handles)
        time.sleep(1)

    if len(window_handles) >= 2:
        raise Exception(f'Expected Page: "{pytest.page}". More windows than expected', window_handles)
    if len(window_handles) == 0:
        raise Exception(f'Expected Page: "{pytest.page}". No windows found', window_handles)
    
    # Valid window
    print("Title Current Window:", driver.title)
    return True


def switch_to_new_window(driver, expected_windows, window_index):
    window_handles = None

    for i in range(5):
        # Get the available windows
        window_handles = driver.window_handles
        print(f"Windows [{i}]:", window_handles)
        # Wait until number of windows expected
        if len(window_handles) >= expected_windows:
            break
        time.sleep(1)

    if len(window_handles) >= expected_windows:
        # Original window
        print("Title Current Window:", driver.title)
        # Switch to new window found
        driver.switch_to.window(window_handles[window_index])
        print("Switched to Window:", window_handles[window_index])
        print("Title New Window:", driver.title)
        return True


def allure_screenshot(driver):
    time.sleep(1)
    allure.attach(
        driver.get_screenshot_as_png(),
        name="Screenshot in: " + pytest.page,
        attachment_type=AttachmentType.PNG
    )
    time.sleep(1)


# INTERACTIONS WITH THE CLIENT APP
# ---------------------------

def get_element_by_position(driver, key, locator, position):
    #(xpath, //div[@class=todo-list-item]//div[@class=button][position])
    locator_by = locator[0]
    print('get_element_by_position : ', locator_by)
    # // div[ @class ="todo-list-item-header"] // h3
    # locator[1]+"[" + position + "]"
    # //div[@class ="todo-list-item"] // div[@ class ="button"][5]
    locator_value = f'({locator[1]})[{position}]'
    print('get_element_by_position : ', locator_value)
    locator_updated = (locator_by, locator_value)

    element = get_element_visible(driver, key, locator_updated)
   # element = scroll_to_get_element_visible(driver, key, locator_updated)
    print('get_element_by_position : ', element)
    return element


def click_element_by_position(driver, key, position):
    validate_screenshot_by_page(driver, key)

    locator = get_locator(key, pytest.page)
    locator_by = locator[0]
    locator_value = f"({locator[1]})[{position}]"
    locator_updated = (locator_by, locator_value)

    element = get_element_clickable(driver, key, locator_updated)
    element.click()
