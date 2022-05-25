from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import pymysql
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os, time, traceback
from arigonggan import models
import bcrypt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import SECRET_KEY


# Create your views here.
def index(request):
    return HttpResponse("replace main")

@method_decorator(csrf_exempt,name='dispatch')
def signup(requset):
    data = json.loads(requset.body)
    userId = data['userId']
    pwd = data['password'].encode('utf-8')
    password_crypt = bcrypt.hashpw(pwd, bcrypt.gensalt())
    password_crypt = password_crypt.decode('utf-8')
    query=(userId,password_crypt)
    try:
        models.usernser(query)
        return JsonResponse({'message':'SUCCESS'},status=200)
    except:
        return JsonResponse({'message':'DBERR'},status=400)

def check_login(userId,password):
    base_path = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(base_path, 'chromedriver')
    service = Service(driver_path)
    opts = webdriver.ChromeOptions()
    chrome_path = os.path.join(base_path, 'Chrome')
    opts.add_argument('headless')
    driver = webdriver.Chrome(service=service, options=opts)
    try:
        driver.get('https://cyber.anyang.ac.kr/Main.do?cmd=viewHome')
        pop = driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/button')
        pop.click()

        ul = driver.find_element(By.CLASS_NAME, 'user_box')
        Id = ul.find_element(By.ID,'id')
        pwd = ul.find_element(By.ID,'pw')

        Id.send_keys(userId)
        pwd.send_keys(password)
        pwd.send_keys(Keys.RETURN)
        try:
            WebDriverWait(driver,3).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
            return 0
        except:
            return 1
    except Exception as e:
        traceback.print_exc()
        return 0
    finally:
        driver.close()
        driver.quit()
