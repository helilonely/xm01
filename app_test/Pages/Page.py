from Pages.mms_page import PageMMS
import Pages
from Pages.search_page import SearchPage

class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def get_mms_page(self):
        return PageMMS(self.driver)

    def get_search_page(self):
        return SearchPage(self.driver)