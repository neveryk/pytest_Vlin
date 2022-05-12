import json
import time
from time import sleep
import pytest
from testcases.conftest import ten,EXCEL
from testcases.conftest import ben
import allure
import random
from common.generate_data import gen
from common.write_excel import wri
import requests

class Test_system():
    @allure.step('客户管理')
    def test_addclient(self):
        # 创建客户
        client_data=gen.addclient_data()
        data=[{"basiceInfo": {"clientName": client_data["clientName"], "accountTypeID":57,"payTaxesCode": client_data["payTaxesCode"],"distributorsID":0,"invoiceBelongingID":61,"clientTypeID": 1, "industryID": 8,"superiorID": 1, "clientSite": [110000, 110100, 110101], "detailedSite": client_data["detailedSite"],"businessIdstr": "1", "liaisonMan": client_data["liaisonMan"], "telephone": client_data["telephone"], "financialIdstr": "1","isFeedback": 0, "saleIdstr": [], "clientBusinessName": "", "clientModeName": "","protocolText": "", "justFiles": 0, "reverseFiles": 0, "legalPerson": "", "legalIDCard": "","ContractFiles": [], "SCFiles": [], "LicenseFiles": [],"ClientRateList": [{"itemCode": "", "ExcessClientRate": "", "ExcessPersonalRate": ""}],"provincesID": 110000, "citiesID": 110100, "areaID": 110101},
               "BusinessInfo":{"clientBusinessID":33,"saleIdstr":"1","termDate":["2021-07-21T16:00:00.000Z","2021-08-30T16:00:00.000Z"],"clientRate":6,"personalRate":3,"ContractFiles":[966],"ICFiles":[],"ExcessLimitAmt":100000,"SCFiles":[],"clientBusinessName":"BtoB业务","clientModeName":"正常客户","termStartDate":"2021-10-22T00:00:00.000Z","termEndDate":"2021-12-31T00:00:00.000Z",
                "ClientRateList":[{"itemCode":"CEQJ-NO1","ExcessClientRate":1,"ExcessPersonalRate":2}],"SceneList":[{"sceneID":142,"SDetailID":"7E5C8593-266B-4E3D-BFE5-2523EF046F34","sceneType":0,"SOrderID":0}]}
                  ,"id":""}]
        res=ten.add_client(data)
        res_json=res.json()
        global company_code
        message=res_json["message"]
        company_code=res_json["data"]
        assert message=="客户业务信息保存成功！"
        data_1=[{"invoiceInfo":{"payTaxesCode":client_data['payTaxesCode'],"address":"地址","officeNumber":client_data["telephone"],"bankofDeposit":"建行","bankAccount":client_data['payTaxesCode']},"id":company_code}]
        res = ten.add_client(data_1)
        data_2=[{"CAInfoList":[{"RemittanceBank":"建行","RemittanceNumber":client_data["bank_code"],"IsOperation":"true"}],"id":company_code}]
        res = ten.add_client(data_2)


    # @allure.step('人员管理')
    # def test_addpeople(self):
    #     # 增加人员
    #     for i in range(0,3):
    #         people_data=gen.addpeople_data()
    #         data=[{"clientID": [int(company_code)], "peopleName": people_data["peoplename"], "cardType": "0", "iDCard": people_data["idcard"], "phone": people_data["phone_num"],"bankName": "建行", "bankCode": people_data["bank_code"], "source": 1, "signFiles": []}]
    #         res=ten.add_people(data)
    #         res_json=res.json()
    #         message=res_json["returnStatus"]
    #         assert message==1
    #
    # @allure.step('订单管理')
    # def test_add_order(self):
    #     # 创建订单
    #     get_people=[{"id":int(company_code)}]
    #     res_people=ten.get_order_data(get_people)
    #     r_j=res_people.json()
    #     peoples_datas=[]
    #     for i in range(len(r_j["data"])):
    #         people_id=r_j["data"][i]["id"]
    #         p={"name": "peopleID", "value": "", "peopleID": people_id, "amt": random.randint(1,500)}
    #         peoples_datas.append(p)
    #     data=[{"clientID":int(company_code),"sceneCode":142,"orderName":"CSC-SUP","content":"000","closeType":1,"totalFee":9,"clientRate":6,"personRate":3,"sceneName":"CJ2105180004-工程服务-工程测量辅助服务","sceneType":0,"peopleDatas":[{"name":"peopleID","value":"","peopleID":"people_id","amt":"o"}]}]
    #     data[0]["peopleDatas"]=peoples_datas
    #     res=ten.add_order(data)
    #     res_json=res.json()
    #     global order_number
    #     order_number=res_json["data"]
    #     order_message=res_json["message"]
    #     assert order_message=='保存成功'
    #
    # @allure.step('账单管理')
    # def test_add_generate(self):
    #     # 系统端生成账单
    #     data=[{"generateCodes":[order_number]}]
    #     res=ten.add_generate(data)
    #     res_json=res.json()
    #     generate_message=res_json["message"]
    #     assert generate_message=='生成1笔对账单'

    # @allure.step('企业钱包充值')
    # def test_recharge(self):
    #     # 充值
    #     data=[{"id":int(company_code),"dealFund":"1.00","dealDate":"2021-08-03 14:48:16","paymentDate":"2021-08-03"}]
    #     for i in range(0,500):
    #         ten.charge_money(data)

#     @allure.step('渠道商管理')
#     def test_savedistrbutors(self):
# #         新增渠道商
#         client_data = gen.addclient_data()
#         data=[{"id":0,"basicInfo":{"isPerson":0,"disName":"渠道商"+client_data["clientName"],"disTaxesCode":client_data["payTaxesCode"],"disType":1,"disMode":"12333123","businessManID":"1","salesManID":"1","agreementFiles":[3545],"salesManName":"系统管理员","businessManName":"系统管理员"},"rateList":[],"dis_agreementFiles":[3545]}]
#         res=ten.save_distributors(data)
#         res_json=res.json()
#         print(res_json)
#
#     def test_GetDistributorsListAll(self):
#         #渠道商查询
#         data=[{"current":1,"pageSize":10}]
#         res=ten.get_DistributorsListAll(data)
#         res_json=res.json()

    # @allure.step('获取银行卡号，生成excel')
    # def test_write_ex(self):
    #     # 获取银行卡号
    #     data = [{"id": 2905}]
    #     res = ten.bank_code(data)
    #     bank_code = res.json()
    #     account = bank_code["data"]["CAInfoList"][0]["RemittanceNumber"]

        # 插入excel数据
        # ex_da = wri.get_data(account)
        # xls_name = EXCEL + '银行到款.xls'

        # 将数据保存到excel
        # sheet_name = 'Sheet1'
        # wri.write_excel_xls(xls_name, sheet_name, ex_da)



    # @allure.step('企业端登录')
    # def test_get_client(self):
    #     data=[{"current":1,"pageSize":10}]
    #     res=ten.get_client(data)
    #     res_json = res.json()
    #     for i in range(0,10):
    #         c_code = res_json["data"][i]["id"]
    #         if int(company_code)==c_code:
    #             global request_token
    #             c_organizingCode = res_json["data"][i]["organizingCode"]
    #             o_code = c_organizingCode[12:18]
    #             request_token = [{"userName": c_organizingCode, "userPwd": o_code}]
    # #
    # @allure.step('企业端核对账单')
    # def test_check_generate(self):
    #     # 企业端核对账单
    #     data = [{"generateCodes": [order_number]}]
    #     res = ben.b_generate(data,request_token)
    #     res_json = res.json()
    #     generate_message = res_json["message"]
    #     assert generate_message == '核对1笔对账单'
    #
    # @allure.step('企业端结算账单')
    # def test_close_bill(self):
    #     # 结算账单
    #     data = [{"generateCode": order_number}]
    #     res = ben.b_close_bill(data,request_token)
    #     res_json = res.json()
    #     generate_message = res_json["message"]
    #     assert generate_message == '结算成功'

    # def test_im_data(self):
    #     url = "http://192.168.8.168:8023/api/PaymentReceived/Import"
    #
    #     payload = {"keyStr": "bc2be7e5-e156-40ad-a353-3bdbdafb0607", "decryptstring": [
    #         'CL8DNabRF1PEyE7y7VEDpHc6nLetOokwtZacsWRFS4FGBBNbatuAuVKe7iWalqgfpisyeS1qMwNTC/hYF9iFVa6MZ3feixGKcFYAmwi3oWB+TDY6y42FDNxKnDm3cPXDcU6aUZBbfMJUSZOVOY6EYRejCntARmjGGkWRcdMnuOE=']}
    #
    #     files = [
    #         ('files', ('银行到款.xls', open('D:/py/pytest_Vlin/data/银行到款.xls', 'rb'), 'application/vnd.ms-excel'))
    #     ]
    #     headers = {
    #         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9zaWQiOiIxIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6ImFkbWluIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiMSIsIklkIjoiMSIsIlVzZXJOYW1lIjoiYWRtaW4iLCJDaGluZXNlTmFtZSI6Iuezu-e7n-euoeeQhuWRmCIsIlVzZXJUeXBlIjoiQmFjayIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdXNlcmRhdGEiOiJ7XCJ1c2VyTmFtZVwiOlwiYWRtaW5cIixcImNoaW5lc2VOYW1lXCI6XCLns7vnu5_nrqHnkIblkZhcIixcInBob25lXCI6XCIxODk3NTg2MjIyMVwiLFwic3RhdHVzXCI6MSxcInN0YWZmSURcIjoxLFwiaWRcIjoxLFwidXNlclR5cGVcIjpcIkJhY2tcIixcImRlcGFydG1lbnRJRFwiOjEsXCJzdGFmZlR5cGVcIjoxLFwiaXNJaWFjXCI6ZmFsc2UsXCJpc0F1dGhlbnRpY2F0aW9uXCI6ZmFsc2V9IiwibmJmIjoxNjM2MDkyODU1LCJleHAiOjE2MzYxMjE2NTUsImlzcyI6IkFzc2lnbmluZ0pvYiIsImF1ZCI6ImFkbWluIn0.KMZl_FgwkdDH-H_qKJIeSNo-_U6Z0Y-VtG7VT06dbvA'}
    #
    #     response = requests.post(url, headers=headers, data=payload, files=files)
        #
        # print(response.text)
        # data=[{"fileType": 0}]
        # ten.tu_le(data)

# t=Test_system()
# t.test_addclient()
# t.test_addpeople()
# t.test_add_order()
# t.test_add_generate()
# t.test_recharge()
# t.test_savedistrbutors()
# t.test_GetDistributorsListAll()
# t.test_write_ex()
# b=B_client()
# t.test_get_client()
# t.test_check_generate()
# t.test_close_bill()
# t.test_im_data()