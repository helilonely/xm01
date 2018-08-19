#coding=utf-8
import Pages
from Base import base_operation

class SearchPage(base_operation.Operate_element):
    def __init__(self,driver):
        self.driver = driver

    def click_search_btn(self):
        """
        点击搜索按钮
        :return: 
        """
        self.click_element(Pages.search_btn)

    def search_info(self,text):
        """
        填写搜索信息，并进行搜索
        :param text: 
        :return: 
        """
        self.send_data(Pages.search_input_text,text)

    def get_result_list(self):
        """
        返回搜索结果列表
        :return: 
        """
        return self.search_elements(Pages.search_result_list)