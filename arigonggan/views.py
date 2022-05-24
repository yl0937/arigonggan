from django.shortcuts import render
from django.http import HttpResponse
import pymysql
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    return HttpResponse("안녕하세요 Pybo에 오신것을 환영합니다.")

@csrf_exempt
def signup(requset):
    if requset.method == 'POST':
        userId=requset.POST['userId']

        user = User(
            userId=userId
        )
        user.save
        print(requset.data)
    return HttpResponse("성공")
