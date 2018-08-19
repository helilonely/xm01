# coding=utf-8
import yaml


def read_data():
    with open("data/data.yaml", 'r') as f:
        data = yaml.load(f)
        print(data)
    return data





if __name__ == '__main__':
    read_data()
