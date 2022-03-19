from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui


def test():
    print('test1')


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    element = driver.find_element(By.ID,'agree')
    rect = element.rect
    pyautogui.click(rect['x'],rect['y'])
    pyautogui.click()

    sleep(2)


