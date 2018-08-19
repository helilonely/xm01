# coding=utf-8
import yaml


class GetData(object):
    def __init__(self, filename):
        self.path = './data/' + filename

    def return_yaml_data(self):
        with open(self.path, "r") as f:
            return  yaml.load(f)

    def return_yaml_data_by_key(self, key):
        with open(self.path, "r") as f:
            return  yaml.load(f).get(key)

