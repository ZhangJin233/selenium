import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract



def test():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    driver.maximize_window()

    t = time.time()
    picture_name = str(t)+'.png'
    driver.save_screenshot(picture_name)

    ce = driver.find_element(By.ID,'captchaimg')
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name)
    img = im.crop((left, top, right, height))

    t2 = time.time()
    picture_name2 = str(t2) + '.png'

    img.save(picture_name2)

    image1 = Image.open(picture_name2)
    text = pytesseract.image_to_string(image1)
    print(text)

    driver.close()

    
