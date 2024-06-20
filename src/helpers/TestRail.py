from typing import Dict, List, Optional
from settings import TESTRAIL

import requests
import json

# Python has a built-in package called re, which can be used to work with Regular Expressions.
import re


class TestRail(object):

    def __init__(self, key):
        self.url = TESTRAIL.get('host')
        self.username = TESTRAIL.get('user')
        self.apikey = key

    @staticmethod
    # The function tags takes an argument expected to
    # be an instance of List[str] Indicated by the type hint tags: List[str].
    # The function is expected to return an instance of Dict[str], as indicated by the -> Dict[str, Optional[str]] hint.
    def get_tags_value(tags: List[str]) -> Dict[str, Optional[str]]:
        """ Get value from list tags for TestRail.
        *Args:* \n
            _tags_ - list of tags.
        *Returns:* \n
            Dict with attributes.
        """
        # dict() -> new empty dictionary
        # dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs
        # dict(iterable) -> new
        # dictionary
        # initialized as if via:
        #     d = {}
        #     for k, v in iterable:
        #         d[k] = v
        attributes: Dict[str, Optional[str]] = dict()
        #attributes = dict()
        print(type(attributes))
        matchers = ['C', 'R']
        for matcher in matchers:
            print( "matchers outer for: " , matcher)
            for tag in tags:
                # print( "tag size = ", len(tags))
                ''' C1234, R1234 '''
                print( "tag = '" + tag + "'")
                """Try to apply the pattern at the start of the string, returning
                    a Match object, or None if no match was found."""
                match = re.match(matcher, tag, re.IGNORECASE)
                print('re.match() : ' , match)
                if match:
                    # assigning value to key
                    ''' attributes['C'] = 1234 '''
                    attributes[matcher] = tag[1:8]
                    # print(' Inside if : ' + tag)
                    print(' Inside if : ' + attributes[matcher])
                    # print(' Inside if KEY : ', attributes.keys())
                    print(' Inside if : ' , attributes)
                    break
                # else:
                #
                #     attributes[matcher] = None
                #     print(' Inside if : ', attributes)
        keys_list = [x for x in attributes]
        print('KEY: ' ,  keys_list )
        return attributes

    def add_result_for_case(self, status, error: str = '', tags=None, screenshot: str = '', version: str = '') -> None:
        # if tags is None:
        #     tags = {}

        print('\n*** TEST RAIL ***')

        tags_value = self.get_tags_value(tags)
        print("tags_value " , tags_value)

        run_id = tags_value['R']
        case_id = tags_value['C']

        assert run_id is not None, 'Error: Please add "runId" tag'
        assert case_id is not None, 'Error: Please add "testCase" tag'
        print('RUN_ID:', run_id)
        print('CASE_ID:', case_id)

        header = {'Content-Type': 'application/json'}

        attachment_id = self.attach_screenshot_to_case(case_id, screenshot)
        body = json.dumps({
            "status_id": 1 if status == 'passed' else 5,
            "version": version,
            "comment": f"{error} \n \n ![Valid XHTML](index.php?/attachments/get/{attachment_id})"
        })

        params = (
            ('/api/v2/add_result_for_case/' + run_id + '/' + case_id, ''),
        )
        response = requests.post(self.url, headers=header, params=params, data=body,
                                 auth=(self.username, self.apikey))

        print('STATUS Add result for case:', response.status_code)
        assert ('No (active) test found for the run' in response.text) is not True, \
            'Error: No (active) test found for the run/case combination'

    def attach_screenshot_to_case(self, case_id: str, screenshot: str = '') -> None:
        params = (
            # (f'/api/v2/add_attachment_to_case/{case_id}')
            ('/api/v2/add_attachment_to_case/{}'.format(case_id))

        )
        file = {'attachment': open(screenshot, 'rb')}
        response = requests.post(self.url, params=params, files=file,
                                 auth=(self.username, self.apikey))
        file['attachment'].close()

        print('STATUS Add attachment to case:', response.status_code)
        assert ('case_id is not a valid test case' in response.text) is not True, \
            'Error: "testCase" is not a valid test case'
        assert ('Authentication failed' in response.text) is False, \
            'Error: Authentication failed: invalid or missing user/password or session cookie'

        try:
            json_data = json.loads(response.text)
            attachment_id = json_data['attachment_id']
            print('Attachment ID:', attachment_id)
            return attachment_id
        except Exception as error:
            print('Error attach_screenshot_to_case function:', error)



if __name__ == "__main__":
    # Example usage
    tags = ['c9090', 'R1234']
    # #tags1: List[str] = []
    # tags1 =  []
    # tags1.append('Sayem')
    # tags1.append('Sayem1')
    # tags1.append(12)
    # print(tags1)
    TESTRAIL_KEY = '8s4jcQOXheMwLEj.1Pgr-y2Q1ld1iTo6eIKp0yZG1'
    testRail = TestRail(TESTRAIL_KEY)
    #testRail.get_tags_value(tags)
    testRail.add_result_for_case('PASSED', 'Ex error', tags,  'Q', 'none')