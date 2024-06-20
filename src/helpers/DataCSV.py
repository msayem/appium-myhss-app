from allure_commons.types import AttachmentType
import allure
import pandas as pd
import os
import pytest
import random


class DataCSV(object):
    def __init__(self):
        self.directory = 'data'
        self.file = f'{self.directory}/{pytest.env}_dataFile.csv'
        self.header = ['environment', 'status', 'userName', 'password', 'firstName', 'lastName']

    def add_row(self, row):
        data = [row]
        dataframe = pd.DataFrame(data)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.exists(self.file):
            dataframe.to_csv(self.file, index=False, mode='a', header=True)
        else:
            dataframe.to_csv(self.file, index=False, mode='a', header=False)

    def validate_record_by_email(self, email):
        dataframe = pd.read_csv(self.file)
        row = dataframe.loc[dataframe['userName'] == email]
        return len(row)

    def get_record_by_email(self, email):
        dataframe = pd.read_csv(self.file)
        row = dataframe.loc[dataframe['userName'] == email]

        assert len(row) != 0, f'There is no record with the "userName" as "{email}"'
        assert len(row) == 1, f'There are more than one record with the "userName" as "{email}"'

        row = row.iloc[0]
        return row

    def get_one_record_by_status(self, status_list):
        dataframe = pd.read_csv(self.file)
        row = dataframe[dataframe['status'].isin(status_list)]

        assert len(row) != 0, f'There is no record with the "status" considered to work with "{status_list}"'

        # select just one record by random index
        row = row.iloc[random.randint(0, len(row) - 1)]

        allure.attach(str(row), name="Pre data", attachment_type=AttachmentType.TEXT)
        print("\nCSV USER:\n" + str(row))

        return row

    def get_one_record_by_status_and_condition(self, status_list, field, value_field):
        dataframe = pd.read_csv(self.file)
        row_status = dataframe[(dataframe['status'].isin(status_list))]
        row = row_status[(dataframe[field] == value_field)]

        assert len(row) != 0, f'There is no record with the "status" considered to work with "{status_list}" ' \
                              f'and "{field}" as "{value_field}"'
        # select just one record by random index
        row = row.iloc[random.randint(0, len(row) - 1)]

        allure.attach(str(row), name="Pre data", attachment_type=AttachmentType.TEXT)
        print("\nCSV USER:\n" + str(row))

        return row

    def update_status_by_email(self, email, new_value):
        dataframe = pd.read_csv(self.file)

        # verify if record exist
        row = dataframe.loc[dataframe['userName'] == email]
        assert len(row) != 0, f'There is no record with the "userName" as "{email}"'
        assert len(row) == 1, f'There are more than one record with the "userName" as "{email}"'

        # update status of the found record
        dataframe.loc[dataframe['userName'] == email, ['status']] = str(new_value)

        # read updated record
        row = dataframe.loc[dataframe['userName'] == email]

        format_row = str(row.to_dict(orient="index"))
        allure.attach(format_row, name="Update status data to " + new_value, attachment_type=AttachmentType.TEXT)

        # write csv file
        dataframe.to_csv(self.file, index=False)

    def update_field_by_email(self, field, email, new_value):
        dataframe = pd.read_csv(self.file)

        # verify if record exist
        row = dataframe.loc[dataframe['userName'] == email]
        assert len(row) != 0, f'There is no record with the "userName" as "{email}"'
        assert len(row) == 1, f'There are more than one record with the "userName" as "{email}"'

        # update status of the found record
        dataframe.loc[dataframe['userName'] == email, [field]] = str(new_value)

        # read updated record
        row = dataframe.loc[dataframe['userName'] == email]
        row = row.reset_index()

        format_row = str(row.to_dict(orient="index"))
        allure.attach(format_row, name=f"Update data in {field} to {new_value}", attachment_type=AttachmentType.TEXT)

        # write csv file
        dataframe.to_csv(self.file, index=False)
