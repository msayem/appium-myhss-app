from pytest_bdd import given, parsers
from src.helpers.DataFixture import DataFixture
from src.helpers.Faker import Faker

import pytest


@given('a user non registered')
def get_non_registered_user():
    Faker.get_data_user()


@given(parsers.parse('a user who is in "{status}" state'))
def find_user_by_specific_status(status):
    # pytest.user = DataCSV().get_one_record_by_status([status])
    pytest.user = DataFixture().get_record_by_status(status)



