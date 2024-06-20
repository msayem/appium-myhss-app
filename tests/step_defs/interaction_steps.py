from pytest_bdd import when, parsers
from pytest_bdd import scenarios

import src.helpers.Common as Common
import pytest

@when('the user resets the app')
def app_reset(driver):
    Common.allure_screenshot(driver)
    driver.terminate_app('edu.hss.myhss.test')
    driver.activate_app('edu.hss.myhss.test')


@when(parsers.parse('the user clicks the "{key}"'))
def click_action(driver, key):
    Common.click_element(driver, key)


@when(parsers.parse('the user fills "{text}" in the "{key}"'))
def type_action(driver, text, key):
    Common.fill_input(driver, text, key)


@when(parsers.parse('the user clicks the "{key_name}" key in virtual keyboard'))
def click_key_virtual_keyboard(driver, key_name):
    driver.hide_keyboard(key_name=key_name)


# INTERACTIONS WITH USER DATA
# ---------------------------

@when(parsers.parse('the user fills data "{user_key}" in the "{field}"'))
def fill_data_in_input(driver, user_key, field):
    Common.fill_input(driver, pytest.user[user_key], field)


@when(parsers.parse('the user clicks the "{key}" from the "{task}" task'))
def click_cta_task(driver, key, task):
    Common.click_element_by_position(driver, key, pytest.task_position)
