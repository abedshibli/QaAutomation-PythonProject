import requests

from Test import conftest


class API_ACTIONS:

    def put_action(self, payload):
        conftest.response = requests.put(conftest.url_api + Test_PostPutDelete.id, json=payload, headers=conftest.header)
