# -*- coding:utf-8 -*-
import allure
from appium import webdriver
import time
# from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
import os
import pytest


class Test_app():
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    @allure.step("这是主测试方法")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @pytest.mark.parametrize("a,b", [(1, 2), (2, 4), (4, 3)])
    def test_parametrize(self, a, b):
        allure.attach("test_parametrize","test_parametrize  01")
        a=a+b
        allure.attach("test_parametrize","test_parametrize  02")
        assert a > b

    @allure.step("测试步骤2")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_2(self, a=2, b=3):
        allure.attach("test_parametrize", "test_parametrize  02")
        assert a > b

    @allure.step("测试步骤3")
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_3(self, a=1, b=3):
        allure.attach("test_3", "测试参数a=%s  b=%s"%(a,b))
        assert a > b