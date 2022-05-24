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
