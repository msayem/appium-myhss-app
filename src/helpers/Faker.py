from faker import Faker
from settings import SECMAIL_SERVICE

import random
import string
import pytest

fake = Faker(['en_US'])
address = SECMAIL_SERVICE
# size of username
len_user = 64
len_domain = 63
len_extension = 63
len_password = 255


class Faker(object):

    @staticmethod
    def get_data_user(field=None, value=None, long=False):
        first_name = fake.first_name()
        last_name = fake.last_name()
        # Username
        if long is False:
            username = f'{first_name}.{last_name}.{str(random.randint(0, 999))}{address}'.lower()
            password = Faker().get_password()
        else:
            user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=len_user))
            domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=len_domain))
            extension = ''.join(random.choices(string.ascii_lowercase, k=len_extension))
            username = f'{user}@{domain}.{extension}'
            password = 'A!' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=len_password - 2))

        user = {
            'env': pytest.env,
            'status': 'PENDING',
            'userName': username,
            'password': password,
            'firstName': first_name,
            'lastName': last_name,
        }
        pytest.user = user
        print("EMAIL:", pytest.user["userName"])

    @staticmethod
    def get_email():
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f'{first_name}.{last_name}{address}'
        return email.lower()

    @staticmethod
    def get_password():
        password = fake.password(length=8, special_chars=True, upper_case=True)
        return password

    @staticmethod
    def get_item(field):
        if field in ("firstName", "nickName"):
            return fake.first_name()
        elif field == "lastName":
            return fake.last_name()

        assert False, f'ERROR: field "{field}" not generate'
