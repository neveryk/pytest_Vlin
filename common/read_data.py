import yaml
from configparser import ConfigParser
import os

class ReadFileData:
    def __init__(self):
        pass

    def load_ini(self, file_path):
        config = ConfigParser()
        config.read(file_path, encoding='utf-8')
        return config

    def load_yaml(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data


data_yaml = ReadFileData()
