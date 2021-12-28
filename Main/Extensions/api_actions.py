import allure
import requests
from Test.conftest import url_api, resource_api, id_api


class API_ACTIONS:
    @staticmethod
    @allure.step("post action")
    def post(userid, id, title, body):
        payload = {"userId": id, "id": str(userid), "title": title, "body": str(body)}
        response = requests.post(url_api + resource_api, data=payload)
        res = response.json()
        response_code = str(response.status_code)
        print("user is created : ", res)
        return response_code

    @staticmethod
    @allure.step("put action")
    def put(userid, id, title, body):
        payload = {"userId": id, "id": str(userid), "title": title, "body": str(body)}
        response = requests.put(url_api + resource_api + id_api, data=payload)
        res = response.json()
        response_code = str(response.status_code)
        print("user is updated : ", res)
        return response_code

    @staticmethod
    @allure.step("delete action")
    def delete(id):
        response = requests.delete(url_api + resource_api + str(id))
        res = response.json()
        response_code = str(response.status_code)
        print("user is deleted : ", res)
        return response_code
