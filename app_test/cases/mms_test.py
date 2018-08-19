# -*- coding:utf-8 -*-
import os, sys

sys.path.append(os.getcwd())

import pytest
from Base.get_driver import get_driver
from Pages import Page
from data.read_data import read_data
from Base.get_data import GetData


def get_text():
    return GetData("data.yaml").return_yaml_data().get('mms_text')

class Test_app():
    def setup_class(self):
        self.page_obj = Page.Page(get_driver('com.android.mms', '.ui.ConversationList'))
        self.mms_obj = self.page_obj.get_mms_page()

    def teardown_class(self):
        print("teardown".center(50, "-"))
        self.page_obj.driver.quit()

    @pytest.mark.run(order=0)
    def test_click_newmms_btn(self):
        self.mms_obj.click_new_mms_btn()
        self.mms_obj.input_recipients("1000")

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("mms_text", get_text())
    def test_params(self, mms_text):
        self.mms_obj.send_mms(mms_text)
        assert mms_text in self.mms_obj.get_mms_list()


if __name__ == '__main__':
    pytest.main("-s mms_test.py")
