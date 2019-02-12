from django.shortcuts import render, HttpResponse
import random
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def dinner(request):
    box = ['chicken', 'pasta', 'pizza', 'hamburger', 'sushi', 'pho']
    menu = random.choice(box)
    # render는 필수인자
    # 1) request, 2) template 파일(html)
    # 3) dictionary : 템프릿에서 쓸 수 있는 값을 정의
    return render(request, 'dinner.html', {'menu':menu, 'box':box})
    # return ('dinner.html', dinner=dinner, box=box)
    # template 은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
    # Django Template Language
    
def you(request, name):
    return render(request, 'you.html', {'name':name})
    
def cube(request, num):
    result = num**3
    return render(request, 'cube.html', {'num':num, 'result':result})
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    msg = request.GET.get('material')
    return render(request, 'pong.html', {'msg':msg})

def user_new(request):
    return render(request, 'user_new.html')
    
def user_read(request):
    id = request.POST.get('id')
    pwd = request.POST.get('pwd')
    return render(request, 'user_read.html', {'id':id, 'pwd':pwd})
    
def template_example(request):
    my_info = {'name': 'yeojin', 'nickname': 'yeojinjok', 'age': 26 }
    my_list = ['짜장면', '짬뽕', '탕수육', '양장피']
    my_sentence = 'Life is short, you need python!'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.datetime.now()
    empty_list = []
    return render(request, 'template_example.html', {'my_info': my_info, 'my_list': my_list, 
    'my_sentence': my_sentence, 'messages': messages, 'datetimenow': datetimenow, 'empty_list': empty_list})
    
def static_example(request):
    return render(request, 'static_example.html')
    
    
