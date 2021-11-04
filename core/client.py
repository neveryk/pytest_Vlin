import requests
import allure
import os
import json

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class Client:
    def __init__(self, host, **kwargs):
        self.host = host
        self.session = requests.session()

    def get(self, url, jsondata=None, **kwargs):
        res = self.session.get(self.host + url, json=jsondata, **kwargs)
        # allure.attach(json.dumps(dict(self.session.headers.items())), 'request-headers', allure.attachment_type.TEXT)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        return res

    def post(self, url, jsondata=None,**kwargs):
        res = self.session.post(self.host + url,data=jsondata,**kwargs)
        # allure.attach(json.dumps(dict(self.session.headers.items())), 'request-headers', allure.attachment_type.TEXT)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        return res

