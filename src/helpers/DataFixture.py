from allure_commons.types import AttachmentType
from data.test_data import TEST_USERS
from data.prod_data import PROD_USERS
import pytest
import allure
import json


class DataFixture(object):

    @staticmethod
    def get_record_by_status(status):
        record = None
        if pytest.env == "test":
            record = TEST_USERS[status]
        if pytest.env == "prod":
            record = PROD_USERS[status]
        print("Test User: ", record)
        ''' json.dumps() method can convert a Python object into a JSON string.'''
        log_record = json.dumps(record, indent=4)
        # allure.attach(str(log_record), name="Pre data", attachment_type=AttachmentType.TEXT)
        allure.attach(log_record, name="Pre data", attachment_type=AttachmentType.TEXT)
        print(f"\n {str.upper(pytest.env)}_USER:", log_record)

        return record
