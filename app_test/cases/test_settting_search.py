# -*- coding:utf-8 -*-
import os,sys
sys.path.append(os.getcwd())
import pytest
import allure
from Base.get_data_by_mysql import GetDataByMySql
from Base.get_driver import get_driver
from Pages.Page import Page


def get_data_by_mysql():
    print(list(GetDataByMySql().query_sth("select input ,expect from search;")))
    return list(GetDataByMySql().query_sth("select input ,expect from search;"))
    # return GetData("data.yaml").return_yaml_data_by_key("search_data")


# @pytest.fixture(params=[{"input":1,"expect":"休眠"},{},{}])
# @pytest.fixture(params=[])
# def read_data(request):
#     return request.param


class Test_app():
    def setup_class(self):
        self.driver = get_driver('com.android.settings', '.Settings')
        self.search_obj = Page(self.driver).get_search_page()

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="点击搜索按钮")
    @pytest.mark.run(order=0)
    def test_click_search_btn(self):
        self.search_obj.click_search_btn()

    @allure.step(title ="输入和搜索")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("input,expect",get_data_by_mysql())
    def test_search(self,input,expect):
        self.search_obj.search_info(input)
        list_result= self.search_obj.get_result_list()
        assert expect in [i.text for i in list_result]


        # @pytest.fixture(autouse=True,scope="class")
        # def click_search_btn(self):
        #     self.locate_fun("id", "com.android.settings:id/search").click()
        #
        # # @pytest.mark.parametrize("read_data",[{"input": 1, "expect": "休眠"},{"input": "ip", "expect": "IP地址"},{"input": "wl", "expect": "WLAN"}])
        # def test_params(self, read_data):
        #     self.locate_fun("id", "android:id/search_src_text").clear()
        #     self.locate_fun("id", "android:id/search_src_text").send_keys(read_data.get("input"))
        #     list_title = self.driver.find_elements_by_id("com.android.settings:id/title")
        #     assert read_data.get("expect") in [i.text for i in list_title]


        # @pytest.mark.run(order=1)
        # def test_scroll3(self):
        #     print("333333333333")
        #     assert 1
        #     pass
        #
        # @pytest.mark.run(order=11)
        # def test_scroll4(self):
        #     print("333333333333")
        #     assert 1


        # #测试滚动scroll
        # @pytest.mark.run(order=3)
        # def test_scroll(self):
        #     wlan = self.locate_fun("xpath", "WLAN")
        #     bat = self.locate_fun("xpath", "电池")
        #     self.driver.scroll(bat, wlan)


        # 测试drag_and_drop
        # def test_drag_and_drop(self):
        #     wlan = self.locate_fun("xpath", "WLAN")
        #     bat = self.locate_fun("xpath", "电池")
        #     self.driver.drag_and_drop(bat, wlan)

        # 测试swipe
        # def test_swipe(self):
        #     wlan = self.locate_fun("xpath", "WLAN")
        #     bat = self.locate_fun("xpath", "电池")
        #     self.driver.swipe(bat.location.get('x'), bat.location.get('y'), wlan.location.get('x'), wlan.location.get('y'))

        # 画图
        # def test_draw(self):
        #     wlan = self.locate_fun("xpath", "WLAN")
        #     bat = self.locate_fun("xpath", "电池")
        #     self.driver.drag_and_drop(bat,wlan)
        #     self.action.tap(self.locate_fun("xpath","安全")).wait(200).perform()
        #     self.action.tap(self.locate_fun("xpath","锁定方式")).wait(200).perform()
        #     self.action.tap(self.locate_fun("xpath","图案")).wait(200).perform()
        #     time.sleep(2)
        #     # WebDriverWait(self.driver, 5).until(lambda x: x.driver.find_element_by_id("com.android.settings:id/lockPattern"))
        #     m=242
        #     n=851
        #     self.action.press(x=m,y=n).move_to(x=m,y=n+480).wait(200).move_to(x=m+480,y=n+480).wait(200).move_to(x=m+480+480,y=n+480).wait(200).move_to(x=m+480+480,y=n+480+480).release().perform()
        #
        #     self.driver.get_screenshot_as_file("./%s.png"%time.time())
