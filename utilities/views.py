from django.shortcuts import render, HttpResponse
import requests
import datetime
import os
import sys
import urllib.request
# Create your views here.
client_id = os.getenv("NAVER_ID")
client_secret = os.getenv("NAVER_SECRET")

def index(request):
    return render(request, 'utilities/index.html')

def bye(request):
    today = datetime.datetime.now()
    lastDay = datetime.datetime(2019, 12, 9)
    result = lastDay - today
    return render(request, 'utilities/bye.html', {'result': result})

def graduation(request):
    today = datetime.datetime.now()
    lastDay = datetime.datetime(2019, 5, 16)
    result = lastDay - today
    return render(request, 'utilities/graduation.html', {'result': result})
    
def imagepick(request):
    url = 'https://picsum.photos/500/500/?random'
    response = requests.get(url)
    result = response.url
    return render(request, 'utilities/imagepick.html', {'result': result})

def today(request):
    key = os.getenv("WEATHER_KEY")
    print(key)
    url = "https://api.openweathermap.org/data/2.5/weather?q=Daejeon&appid=" + key
    response = requests.get(url).json()
    today = datetime.datetime.now()
    main = response["weather"][0]["main"]
    desc = response["weather"][0]["description"]
    return render(request, 'utilities/today.html', {'hour': today.hour, 'minute': today.minute, 'second': today.second, 'main': main, 'desc': desc})
    
def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts': fonts})
    
def ascii_make(request):
    text = request.POST.get('text')
    font = request.POST.get('selectedFont')
    url = f"http://artii.herokuapp.com/make?text={text}&font={font}"
    response = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'response': response})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    korean = request.POST.get('korean')
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": korean
    }
    papagoResponse = requests.post(papago_url, headers=headers, data=data).json()
    reply_text = papagoResponse["message"]["result"]["translatedText"]
    return render(request, 'utilities/translated.html' ,{'result': reply_text})