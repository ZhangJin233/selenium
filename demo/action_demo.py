from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('http://sahitest.com/demo/clicks.htm')
        self.driver.maximize_window()

    def test_action(self):
        btn = self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn)

        sleep(2)

        rightClicks = self.driver.find_element(By.XPATH,'/html/body/form/input[4]')
        ActionChains(self.driver).context_click(rightClicks)

        sleep(2)

    def test_keychain(self):
        self.driver.get('http://www.google.com')
        kw = self.driver.find_element(By.NAME,'q')
        kw.send_keys('selenium')
        kw.send_keys(Keys.CONTROL,'a')
        sleep(2)
        kw.send_keys(Keys.CONTROL,'x')
        sleep(2)
        kw.send_keys(Keys.CONTROL,'c')
        sleep(2)

    def test_mouse_move(self):
        self.driver.get('http://sahitest.com/demo/mouseover.htm')
        ele = self.driver.find_element(By.XPATH,'/html/body/form/input[1]')
        ActionChains(self.driver).move_to_element(ele).perform()
        sleep(2)



if __name__ == '__main__':
    case = TestCase()
    case.test_mouse_move()
    case.driver.quit()