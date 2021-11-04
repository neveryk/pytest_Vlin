import json
from core.client import Client
from common.Rsa import rsa
import allure

class Benapi(Client):
    def __init__(self, host, **kwargs):
        super(Benapi, self).__init__(host, **kwargs)

    def imple_method(self, data,token_data):
        token = self.get_token(token_data)
        herder = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer " + token
        }
        rsa_str = self.get_rsa_str()
        json_data = json.dumps(data)
        r_data = rsa.rsa_encrypt(data=json_data, all_key=rsa_str)
        request_data = "{\"keyStr\":\"" + r_data['key'] + "\",\"decryptstring\": " + r_data['Rsa_data'] + "}"
        return [request_data, herder]

    def get_rsa_str(self):
        res = self.get('/api/UserBack/GetRSA')
        respons_json = json.loads(res.text)
        rasStr = respons_json["data"]["rasStr"]
        KeyStr = respons_json["data"]["KeyStr"]
        return {"rasstr": rasStr, "keystr": KeyStr}

    def get_token(self,data):
        rsa_str = self.get_rsa_str()
        herder = {
            "Content-Type": "application/json; charset=utf-8"
        }
        json_data = json.dumps(data)
        r_data = rsa.rsa_encrypt(data=json_data, all_key=rsa_str)
        request_data = "{\"keyStr\":\"" + r_data['key'] + "\",\"decryptstring\": " + r_data['Rsa_data'] + "}"
        respons = self.post('/api/UserClient/UserClientLogin', jsondata=request_data, headers=herder)
        r_json = respons.json()
        token = r_json["data"]["toKen"]
        return token

    def b_generate(self,data,token_data):
        # 核对账单
        re_data = self.imple_method(data,token_data)
        return self.post('/api/Generate/CheckBill', jsondata=re_data[0], headers=re_data[1])

    def b_close_bill(self,data,token_data):
        # 结算账单
        re_data = self.imple_method(data,token_data)
        return self.post('/api/Generate/RePostCloseBill', jsondata=re_data[0], headers=re_data[1])