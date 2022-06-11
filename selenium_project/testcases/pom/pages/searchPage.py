from selenium.webdriver.common.by import By
from testcases.pom.pages.basePage import BasePage


class SearchPage(BasePage):
    search_input = (By.ID,'kw')
    search_button = (By.ID,'su')

    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def go_to_baidu(self):
        self.driver.get('http://www.baidu.com')

    def input_kw(self):
        self.type_text('selenium',*self.search_input)

    def click_button(self):
        self.click(*self.search_button)
