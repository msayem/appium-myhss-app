from pytest_bdd import then, parsers
from settings import *

import src.helpers.Common as Common
import pytest
import time
import json


@then(parsers.parse('it displays the "{page_name}" Screen'))
def display_page(driver, page_name):
    Common.validate_page(driver, page_name)
    pytest.page = page_name


@then(parsers.parse('element "{key}" is displayed'))
def displayed_element(driver, key):
    locator = Common.get_locator(key, pytest.page)
    if pytest.page in ['Menu', 'Resources']:
        Common.scroll_to_get_element_visible(driver, key, locator)
    else:
        Common.get_element_visible(driver, key, locator)


@then(parsers.parse('text "{expected_text}" is displayed into the "{key}"'))
def displayed_text_key(driver, expected_text, key):
    locator = Common.get_locator(key, pytest.page)
    if pytest.page in ['Menu', 'Resources']:
        element = Common.scroll_to_get_element_visible(driver, key, locator)
    else:
        element = Common.get_element_visible(driver, key, locator)
    Common.verify_element_text(key, expected_text, element)


@then(parsers.parse('"{key}" has the value "{expected_text}"'))
def value_text_key(driver, key, expected_text):
    locator = Common.get_locator(key, pytest.page)
    element = Common.get_element_visible(driver, key, locator)
    for i in range(5):
        if len(element.get_attribute("value")) > 0:
            break
        time.sleep(1)
        i += 1
    value = element.get_attribute('value')

    assert value == expected_text, \
        f'The element "{pytest.page}.{key}" not contain the expected text: "{expected_text}". ' \
        f'Text found "{value}"'


# USER DATA VALIDATION
# ---------------------------
@then(parsers.parse('data "{user_key}" is displayed into the "{key}"'))
def displayed_user_data(driver, user_key, key):
    expected_text = pytest.user[user_key]
    locator = Common.get_locator(key, pytest.page)
    element = Common.get_element_visible(driver, key, locator)
    Common.verify_element_text(key, expected_text, element)


# APP DATA VALIDATION
# ---------------------------
@then(parsers.parse('app "{version}" is displayed into the "{key}"'))
def displayed_app_data(driver, version, key):
    if pytest.host == "localhost":
        expected_text = IOS_SIMULATOR[pytest.env][version]
    else:
        expected_text = BROWSER_STACK[pytest.env]['iOSBuildVersion']#pytest.bs_app_build_version

    locator = Common.get_locator(key, pytest.page)
    element = Common.get_element_visible(driver, key, locator)
    Common.verify_element_text(key, expected_text, element)


# time is within "00:00" and "11:59"
@then(parsers.parse('greeting "{expected_text}" is displayed into the "{key}" if device time is within "{start}" and "{end}"'))
def displayed_text_by_time(driver, expected_text, key, start, end):
    locator = Common.get_locator(key, pytest.page)
    element = Common.get_element_visible(driver, key, locator)
    current_text = element.text
    print("Current txt: ", current_text)

    time_str = driver.get_device_time('HH:mm')
    time_obj = time.strptime(time_str, '%H:%M')
    print("Device time:", time_str)
    validation = False
    start_obj = time.strptime(start, '%H:%M')
    end_obj = time.strptime(end, '%H:%M')
    #if time_obj >= start_obj and time_obj <= end_obj:
    if start_obj <= time_obj <= end_obj:
        validation = True
        assert current_text == expected_text, \
            f'The element "{pytest.page}.{key}" not contain the expected text: "{expected_text}". ' \
            f'Text found "{current_text}"'
    print(f'Validation: "{expected_text}" ({validation})')


@then(parsers.parse('"{key}" is selected'))
def validate_tab_selected(driver, key):
    locator = Common.get_locator(key, pytest.page)
    element = Common.get_element_visible(driver, key, locator)
    found = False
    class_desc = None
    for i in range(5):
        class_desc = element.get_attribute("class")
        if "selected" in class_desc:
            found = True
            break
        time.sleep(1)
        i += 1

    assert found, f'The "{pytest.page}.{key}" is not selected. ' \
                  f'Class found: "{class_desc}"'


@then(parsers.parse('"{task}" task is displayed in To Do List'))
def displayed_app_data(driver, task):
    expected_task_title = pytest.user['tasks'][task]['title']
    expected_task_cta = pytest.user['tasks'][task]['cta']

    key_title = 'TaskTitle'
    locator = Common.get_locator(key_title, pytest.page)
    elements = Common.get_elements_visible(driver, key_title, locator)
    # print(elements.count())

    list_elements = []
    found = False
    pytest.task_position = None
    # key_cta = 'TaskButton'
    current_text = None

    # filtered_list = [e for element in elements if element['text'] == 'abc']
    # list(filter(lambda x: x.get('text', '') == 'abc', listpost))
    # result = filter(lambda x: x == expected_task_title,  elements)
    # # current_text = elements
    # print(result)

    for index, element in enumerate(elements):
        list_elements.append(element.text)
        if element.text == expected_task_title:
            print("i am inside if" , index)
            pytest.task_position = index + 1
            found = True
            # locator = Common.get_locator(key_cta, pytest.page)
            # print('displayed_app_data(driver, task): ', locator)
            # #Locator Strategy 'css selector,.todo-list-item-actions .button'
            # # is not supported for this session;
            # current_text = element.find_element(locator).text
            # print(current_text)

    print("Task List:", json.dumps(list_elements, indent=4))
    print('Task Position Found:', pytest.task_position)

    assert found, \
        f'Element "{pytest.page}.{key_title}" dose not contain the expected text: "{expected_task_title}".'

    key_cta = 'TaskButton'
    locator = Common.get_locator(key_cta, pytest.page)

    print ('displayed_app_data(driver, task): ' , locator)
    element = Common.scroll_to_get_element_visible(driver, key_cta, locator)
    element = Common.get_element_by_position(driver, key_cta, locator, pytest.task_position)
    current_text = element.text
    print(current_text)

    assert current_text == expected_task_cta, \
        f'The element "{pytest.page}.{key_cta}" not contain the expected text: "{expected_task_cta}". ' \
        f'Text found "{current_text}"'
