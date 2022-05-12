import json
import requests


class CARequest:
    def __init__(self, url: str, headers: dict, data: dict, method: str):
        self.__url = url
        self.__headers = headers
        self.__data = json.dumps(data)
        self.__method = method
        self.__content = ''
        self.__status_code = ''

    def request(self):
        if self.__method == 'GET':
            get_request = requests.get(url=self.__url, headers=self.__headers, data=self.__data)
            self.__content = get_request.json()
            self.__status_code = get_request.status_code
        elif self.__method == 'POST':
            post_request = requests.post(url=self.__url, headers=self.__headers, data=self.__data)
            self.__content = post_request.json()
            self.__status_code = post_request.status_code

    def get_content(self):
        return self.__content

    def get_status_code(self):
        return self.__status_code
