from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/selectTest.htm')
        self.driver.maximize_window

    def test_select(self):
        se = self.driver.find_element(By.ID,'s1Id')
        select = Select(se)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('o1')
        # sleep(2)
        # select.select_by_visible_text('o3')
        # sleep(2)

        # for i in range(2):
        #     select.select_by_index(i)
        #     sleep(2)
        # sleep(2)

        # select.deselect_all()
        # sleep(2)
        for option in select.options:
            print(option.text)
        self.driver.quit

if __name__ == '__main__':
    case = TestCase()
    case.test_select()