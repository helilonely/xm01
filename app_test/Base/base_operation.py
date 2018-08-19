# -*- coding:utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait


class Operate_element():
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, location, timeout=15, poll_frequency=1):
        """"
        定位元素
        :param location: （By.ID,value）
        :param timeout: 
        :param poll_frequency: 
        :return: """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*location))

    def click_element(self, location,timeout=15, poll_frequency=1):
        """
        点击元素
        :param location: 
        :return: 
        """
        self.search_element(location,timeout, poll_frequency).click()

    def send_data(self, location, text,timeout=15, poll_frequency=1):
        """
        元素输入
        :param location: 
        :param text: 
        :return: 
        """
        self.search_element(location,timeout, poll_frequency).send_keys(text)

    def search_elements(self, location, timeout=15, poll_frequency=1):
        """"
        定位元素
        :param location: （By.ID,value）
        :param timeout: 
        :param poll_frequency: 
        :return: """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*location))