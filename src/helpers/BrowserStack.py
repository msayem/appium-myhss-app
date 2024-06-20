from requests.auth import HTTPBasicAuth
from browserstack.local import Local
import requests
import json


class BrowserStack(object):
    local = None

    def __init__(self, bs_user, bs_api):
        self.bs_username = bs_user
        self.bs_apikey = bs_api
        # self.local = None

    def update_test_status(self, endpoint, session_id, status, error):
        print('\n*** BROWSER STACK ***')
        print('Error: ' + str(error))
        web_server = f"https://api.browserstack.com/automate/sessions/{session_id}.json"
        mobile_server = f"https://api-cloud.browserstack.com/app-automate/sessions/{session_id}.json"
        url = mobile_server if endpoint == 'app' else web_server

        headers = {'Content-Type': 'application/json'}
        ''' json.dumps() method can convert a Python object into a JSON string.
        json.dump() method can be used for writing to JSON file.'''
        payload = json.dumps({
            "status": status,
            "reason": error
        })
        response = requests.request(
            "PUT", url,
            auth=HTTPBasicAuth(self.bs_username, self.bs_apikey),
            headers=headers, data=payload)
        print('STATUS Add test status:', response.status_code)
       # print('Response in text:', response.text)
        print("RESPONSE : " , json.dumps(response.json(), indent=4, sort_keys=True))
        # Use the json module to load CKAN's response into a dictionary.
        '''json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary '''
        response_dict = json.loads(response.text)
        for i in response_dict['automation_session']:
            print("key: " + i, "val: " , response_dict['automation_session'][i])

    @staticmethod
    def get_video_url(session_id):
        # https://automate.browserstack.com/s3-upload/s-video-logs-use/s3/f13eb1dd728cbc4b97f3d39439b10395a0ae3b1c/video-f13eb1dd728cbc4b97f3d39439b10395a0ae3b1c.mp4
        video_url = f"https://automate.browserstack.com/s3-upload/bs-video-logs-use/s3/{session_id}/video-{session_id}.mp4"
        print("VIDEO:", video_url)
        return video_url

    def start_local(self):
        try:
            self.local = Local()
            local_args = {"key": self.bs_apikey, "forcelocal": "true"}
            self.local.start(**local_args)
            print("BrowserStack Local started successfully")
        except Exception as e:
            print("Failed to start BrowserStack Local:", e)

    def stop_local(self):
        try:
            if self.local is not None:
                self.local.stop()
                print("BrowserStack Local stopped successfully")
            else:
                print("BrowserStack Local is not running.")
        except Exception as e:
            print("Failed to stop BrowserStack Local:", e)
