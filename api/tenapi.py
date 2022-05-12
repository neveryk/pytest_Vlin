import json
from ast import literal_eval

import requests

from core.client import Client
from common.Rsa import rsa
import allure

class Tenapi(Client):
    def __init__(self, host, **kwargs):
        super(Tenapi, self).__init__(host, **kwargs)
    def method(self,data):
        rsa_str = self.get_rsa_str()
        json_data = json.dumps(data)
        r_data = rsa.rsa_encrypt(data=json_data, all_key=rsa_str)
        request_data = "{\"keyStr\":\"" + r_data['key'] + "\",\"decryptstring\": " + r_data['Rsa_data'] + "}"
        return request_data

    def excel_method(self,data):
        rsa_str = self.get_rsa_str()
        json_data = json.dumps(data)
        r_data = rsa.rsa_encrypt(data=json_data, all_key=rsa_str)
        request_data = {"keyStr":r_data['key'] ,"decryptstring": r_data['Rsa_data']}
        return request_data

    def get_rsa_str(self):
        res=self.get('/api/UserBack/GetRSA')
        respons_json = json.loads(res.text)
        rasStr = respons_json["data"]["rasStr"]
        KeyStr = respons_json["data"]["KeyStr"]
        return {"rasstr":rasStr,"keystr":KeyStr}

    def get_token(self):
        data=[{"username": "admin", "userPwd": "123456"}]
        rsa_str=self.get_rsa_str()
        herder = {
            "Content-Type": "application/json; charset=utf-8"
        }
        json_data=json.dumps(data)
        r_data=rsa.rsa_encrypt(data=json_data,all_key=rsa_str)
        request_data="{\"keyStr\":\""+r_data['key']+"\",\"decryptstring\": "+r_data['Rsa_data']+"}"
        print(request_data)
        respons=self.post('/api/UserBack/Login', jsondata=request_data, headers=herder)
        text = json.loads(respons.text)
        token1 = text["data"]["toKen"]
        herder_token = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + token1
        }
        return herder_token

    def add_client(self,data):
        re_token=self.get_token()
        re_data=self.method(data)
        return  self.post('/api/Client/Save', jsondata=re_data, headers=re_token)
    #
    def get_client(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/Client/GetDataList', jsondata=re_data, headers=re_token)

    def add_people(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/People/SavePeople', jsondata=re_data, headers=re_token)

    def get_order_data(self,people):
        re_token = self.get_token()
        re_data = self.method(people)
        return self.post('/api/People/SeePeople', jsondata=re_data, headers=re_token)
    #
    def add_order(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/Order/AddFinishOrder', jsondata=re_data, headers=re_token)

    def add_generate(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/Generate/GenerateBill', jsondata=re_data, headers=re_token)

    def charge_money(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/DealRecord/rechargeMoney', jsondata=re_data, headers=re_token)

    def save_distributors(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/Distributors/SaveDistributors', jsondata=re_data, headers=re_token)

    def get_DistributorsListAll(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.get('/api/Distributors/GetDistributorsListAll', jsondata=re_data, headers=re_token)

    def bank_code(self,data):
        re_token = self.get_token()
        re_data = self.method(data)
        return self.post('/api/Client/GetViewModel', jsondata=re_data, headers=re_token)

    def tu_le(self,data):
        files = [
            ('files', ('银行到款.xls', open('D:/py/pytest_Vlin/data/银行到款.xls', 'rb'), 'application/vnd.ms-excel'))
        ]

        re_token = self.get_token()
        token={"Authorization":re_token["Authorization"],"Content-Type":"multipart/form-data;"}

        re_data = self.excel_method(data)

        a=re_data["decryptstring"]

        b=literal_eval(a)

        re_data["decryptstring"]=b

        print(re_data)



        # requ_data["file"]=len(files)



        url = "http://192.168.8.168:8023/api/PaymentReceived/Import"



        response = requests.post(url, headers=token, data=re_data,files=files)

        print(response.text)

