# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from Base.base_operation import Operate_element
import Pages


class PageMMS(Operate_element):
    def __init__(self, driver):
        Operate_element.__init__(self, driver)
        # self.driver = driver

    def click_new_mms_btn(self):
        self.click_element(Pages.new_mms_btn)

    def input_recipients(self, recipient):
        """
        输入短信接收者
        :param recipient: 短信接收者
        """
        self.send_data(Pages.mms_recipients_editor, recipient)

    def send_mms(self, text):
        """
        发送短信
        :param text: 短信内容
        :return: 无
        """
        self.send_data(Pages.embedded_text_editor, text)
        self.click_element(Pages.send_button_sms)

    def get_mms_list(self):
        """
        获取短信的文本内容
        :return: 获取短信的文本内容列表
        """
        list_ele = self.search_elements(Pages.list_sms)
        return [i.text for i in list_ele]
