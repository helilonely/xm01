#coding=utf-8
import Api
import os, sys
import time
import logging
import requests
from Base.get_data_from_yml import ReadData


class DeparmentsApi(ReadData):

    def __init__(self):
        ReadData.__init__(self,"departments.yml", "new_department_value")
        self.add_json = self.read_data()


    @staticmethod
    def assert_status_code(status_code, code):
        try:
            assert status_code == code
        except Exception as e:
            logging.debug(time.strftime("%Y-%m-%d %H_%M_%S\t"))
            logging.error("断言异常：返回状态码%s!=%s"%(status_code,code))
            raise

    #添加department
    def add_department(self):
        res =requests.post(Api.department_url,json=self.add_json)
        return res

    # 删除添加的department
    def delete_department(self):
        dep_id_list = [i.get("dep_id") for i in self.add_json["data"]]
        if len(dep_id_list) == 1:
            delete_str1=Api.department_url+dep_id_list[0]+"/"
        elif len(dep_id_list)>1:
            delete_str1=Api.department_url+r"?$dep_id_list="+','.join(dep_id_list)
       # print("_____****"+delete_str1+"_____****")
        res = requests.delete( delete_str1)
        return res

    #查询特定的department
    def lookup_theDepartment(self,dep_id="hahaha5"):
        return requests.get(Api.department_url +dep_id+"/")

