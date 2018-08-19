# -*- coding:utf-8 -*-
import os, sys

sys.path.append(os.getcwd())
from appium.webdriver.common.touch_action import TouchAction
import pytest

from Base.get_driver import get_driver
from Pages import Page


class Test_app():
    def setup_class(self):
        self.page_obj = Page.Page(get_driver("com.android.mms", '.ui.ConversationList'))
        self.mms_obj = self.page_obj.get_mms_page()
        self.mms_obj.click_new_mms_btn()
        self.mms_obj.input_recipients("10000")
        print("\n", "setup".center(50, "-"))

    def teardown_class(self):
        print("teardown".center(50, "-"))
        self.page_obj.driver.quit()

    # #打开新建短信，并输入接收者为10086
    # @pytest.fixture(scope="class", autouse=True)
    # def open_mms_page(self):
    #     self.mms_obj=self.page_obj.get_mms_page()
    #     self.mms_obj.click_new_mms_btn()
    #     self.mms_obj.input_recipients("10000")


    # 测试发短信
    @pytest.mark.parametrize("text", ["d1", "d2", "d3"])
    def test_01(self, text):
        self.mms_obj.send_mms(text)
        assert text in self.mms_obj.get_mms_list()


if __name__ == '__main__':
    pytest.main("-s mms_test02.py")
