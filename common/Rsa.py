import math
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
import json

class Rsa_Encryption():
    def rsa_encrypt(self,data,all_key):
        """校验RSA加密 使用公钥进行加密"""
        requests_data=[]
        cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(all_key["rasstr"]))
        if len(str(data)) < 100:
            cipher_text = base64.b64encode(cipher.encrypt(data.encode())).decode()
            requests_data.append(cipher_text)
            str_requests_data = str(requests_data)
            return {"Rsa_data":str_requests_data,"key":all_key["keystr"]}
        else:
            st_data=data
            num = math.ceil(len(str(st_data)) / 100)
            for i in range(0, num):
                data_li = str(data)[100 * i:100 * (i + 1)]
                cipher_text = base64.b64encode(cipher.encrypt(data_li.encode())).decode()
                requests_data.append(cipher_text)
            str_requests_data=str(requests_data)
        return {"Rsa_data":str_requests_data,"key":all_key["keystr"]}



rsa=Rsa_Encryption()
