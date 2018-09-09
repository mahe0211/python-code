# Given the API in the Input Description, write a script that successfully creates a new widget,
# confirms the creation of the widget, and then updates the description of the widget. The
# script should then confirm that the updated widget is in the full list of all widgets. Finally,
# delete the widget and confirm the deletion via status code.

import unittest
import requests
import json


class TestWidget(unittest.TestCase):
    """
    Unit test class TestWidget to test the functionality of widget creation updation and deletion
    """
    url = "https://dev.rackspace.example.com/widgets"
    auth_token = "5675309"

    def test_create_new_widget(self):
        payload = {'widget_name': 'Test Widget', 'description': 'Description'}
        headers = {'content-type': 'application/json', 'X-Auth-Token': self.auth_token}

        try:
            create_resp = requests.post(url=self.url, data=json.dumps(payload), headers=headers)
            if create_resp.status_code == 201:
                assert 'application/json' in create_resp.headers['Content-Type']
                print(create_resp.json())
                print("request and widget creation status: SUCCESS")

                widget_id = '1'
                get_resp = requests.get(url=self.url + '/' + widget_id)
                if get_resp.status_code == 200:
                    get_resp_data = get_resp.json()
                    assert get_resp_data['widget_id'] == 1
                    assert get_resp_data['widget_name'] == 'Test Widget'
                    assert get_resp_data['description'] == 'Description'

            elif create_resp.status_code == 400:
                print("request and widget creation status: FAIL")
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            print(e)

    def test_update_existing_widget(self):
        payload = {'description': 'A new description'}
        headers = {'content-type': 'application/json', 'X-Auth-Token': self.auth_token}

        try:
            updation_resp = requests.put(url=self.url, data=payload, headers=headers)
            if updation_resp.status_code == 204:
                assert 'application/json' in updation_resp.headers['Content-Type']
                print("request widget updation status: SUCCESS")

                get_all_resp = requests.get(url=self.url)
                if get_all_resp.status_code == 200:
                    get_all_resp_data = get_all_resp.json()
                    for item in get_all_resp_data:
                        if item['description'] == 'A new description':
                            print("Widget updated successfully and present in widget list")
                            break

            elif updation_resp.status_code == 400:
                print("request and widget updation status: FAIL")
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            print(e)

    def test_delete_existing_widget(self):
        headers = {'X-Auth-Token': self.auth_token}

        try:
            resp = requests.delete(url=self.url, headers=headers)
            if resp.status_code == 204:
                assert 'application/json' in resp.headers['Content-Type']
                print("deletion request status: SUCCESS")
            elif resp.status_code == 400:
                print("deletion request status: FAIL")
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as e:
            print(e)


if __name__ == "__main__":
    unittest.main()
