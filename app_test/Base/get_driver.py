from appium import webdriver
def get_driver(appPackage,appActivity):
    desired_caps = {}
    desired_caps["platformName"] = 'Android'
    desired_caps["platformVersion"] = '5.1'
    desired_caps["deviceName"] = 'test_machine'
    desired_caps["appPackage"] = appPackage
    desired_caps["appActivity"] = appActivity
    desired_caps["unicodeKeboard"] = True
    desired_caps["resetKeboard"] = True
    return  webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)