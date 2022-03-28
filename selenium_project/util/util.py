from PIL import Image
import os
import time
from selenium.webdriver.common.by import By
import pytesseract





def get_coder(driver,id):

    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots'
    picture_name1 = str(t) +'.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element(By.ID,id)
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))

    t2 = time.time()
    picture_name2 = str(t2) + '.png'

    time.sleep(2)
    img.save(picture_name2)

    image1 = Image.open(picture_name2)
    text = pytesseract.image_to_string(image1)
    return text