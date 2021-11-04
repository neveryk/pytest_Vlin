import random
import datetime
from faker import Faker
f=Faker(locale='zh-CN')
class Generate_Data():
    def addclient_data(self):
        client="跳跳蛙"+ f.company()
        bank_card=str(random.randint(1000000000000000, 9999999999999999))+"QA"
        bank_code = random.randint(6200000000000000, 6299999999999999)
        address=f.address()
        money=random.randint(1,500)
        name=f.name()
        ph_number=f.phone_number()
        return {"clientName":client,"payTaxesCode":bank_card,"detailedSite":address,"liaisonMan":name,"telephone":ph_number,"bank_code":str(bank_code),"money":money}
    def addpeople_data(self):
        people_name=f.name()
        bank_code = random.randint(6200000000000000, 6299999999999999)
        phone_num=f.phone_number()
        sfz = f.ssn()
        return {"peoplename":people_name,"bank_code":str(bank_code),"phone_num":phone_num,"idcard":sfz}
gen=Generate_Data()
