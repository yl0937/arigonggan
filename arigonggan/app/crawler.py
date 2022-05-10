import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(base_path, 'chromedriver')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
def check_login(userId,password):
    try:
        driver.get('https://cyber.anyang.ac.kr/Main.do?cmd=viewHome')
        time.sleep(1)

        pop = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/button')
        pop.click()

        ul = driver.find_element(By.CLASS_NAME, 'user_box')
        Id = ul.find_element(By.ID,'id')
        pwd = ul.find_element(By.ID,'pw')

        Id.send_keys(userId)
        pwd.send_keys(password)
        pwd.send_keys(Keys.RETURN)
        time.sleep(5)
        # try:
        #     driver.switch_to.alert()
        #     print('다시 입력하세요')
        # except:
        #     print('성공')
    except Exception as e:
        traceback.print_exc()
    finally:
        driver.close()
        driver.quit()
