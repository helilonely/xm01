import yaml


class ReadData(object):
    def __init__(self,filename,param_name):
        self.filedir = "./data/"+filename
        self.param_name=param_name

    #�Ӹ����������ļ�·������ȡ��Ӧ������������
    def read_data(self):
        with open(self.filedir,"r") as f:
            data=yaml.load(f)
        return data[self.param_name]
