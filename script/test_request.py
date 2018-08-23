# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.getcwd())
from  Api.Api import GetApis
import pytest
import allure

class TestApi(object):
    #开始增加若干数据
    def setup_class(self):
        self.deparment_api = GetApis().get_department_api()


    @allure.step(title="添加数据")
    @pytest.mark.run(order=0)
    def test_add_departmensts(self):
        allure.attach("向接口发送数据并且执行添加","")
        res = self.deparment_api.add_department()
        print()
        print(res.text, "status_code:", res.status_code, '\n')
        allure.attach("断言结果", "状态码%s= 201"%res.status_code)
        self.deparment_api.assert_status_code(res.status_code, 201)
        print('_' * 50)

    @pytest.mark.run(order=-1)
    @allure.step(title="删除数据")
    def test_delete_department(self):
        res = self.deparment_api.delete_department()
        print(res.text, "status_code:", res.status_code, '\n')
        self.deparment_api.assert_status_code(res.status_code, 204)


    # # 修改学院信息
    # def test_put(self):
    #     res=requests.put("".join([Api.department_url,self.dep_id,"/"]), json=Api.to_put_department_value)
    #     print(res.text,"status_code:",res.status_code, '\n')
    #     self.deparment_api.assert_status_code(res.status_code, 200)
    #

    #查询特定学院信息
    @allure.step(title="执行查询")
    def test_lookup(self):
        res = self.deparment_api.lookup_theDepartment()
        print(res.text, "status_code:", res.status_code, '\n')
        self.deparment_api.assert_status_code(res.status_code, 200)


