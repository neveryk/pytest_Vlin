from api.tenapi import Tenapi
import os
from common.read_data import data_yaml
from api.tenapi import Tenapi
from common.generate_data import Generate_Data
from api.b_client import Benapi

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')

def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_name)
    yaml_data = data_yaml.load_yaml(data_file_path)
    return yaml_data

base_data = get_data('login_data.yml')

HOST=data_yaml.load_ini(data_file_path)["host"]["BASEURL"]
EXCEL=data_yaml.load_ini(data_file_path)["host"]["EXCELURL"]

ten=Tenapi(HOST)
ben=Benapi(HOST)
gen=Generate_Data()