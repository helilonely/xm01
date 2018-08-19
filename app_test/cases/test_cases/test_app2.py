# -*- coding:utf-8 -*-
from appium import webdriver
import time
# from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
import os
import pytest



class Test_app():
    def setup_class(self):
        desired_caps = {}
        desired_caps["platformName"] = 'Android'
        desired_caps["platformVersion"] = '5.1'
        desired_caps["deviceName"] = 'test_machine'
        desired_caps["appPackage"] = 'com.android.settings'
        desired_caps["appActivity"] = '.Settings'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.action = TouchAction(driver=self.driver)
        self.driver.implicitly_wait(3)
        print("\n", self.driver.device_time, "setup".center(50, "-"))

    def teardown_class(self):
        print("teardown".center(50, "-"))
        self.driver.quit()

    def locate_fun(self, ty, ty_val):
        if ty == 'id':
            return self.driver.find_element_by_id(ty_val)
        if ty == 'class':
            return self.driver.find_element_by_class_name(ty_val)
        if ty == 'xpath':
            return self.driver.find_element_by_xpath("".join(["//*[contains(@text,'", ty_val, "')]"]))

    # #测试滚动scroll
    # @pytest.mark.run(order=3)
    # def test_scroll(self):
    #     wlan = self.locate_fun("xpath", "WLAN")
    #     bat = self.locate_fun("xpath", "电池")
    #     self.driver.scroll(bat, wlan)

    @pytest.fixture(autouse=True, scope="class")
    def before(self):
        print("***登录操作****\n")


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
