from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def dinner(request):
    box = ['chicken', 'pasta', 'pizza', 'hamburger', 'sushi', 'pho']
    menu = random.choice(box)
    # render는 필수인자
    # 1) request, 2) template 파일(html)
    # 3) dictionary : 템프릿에서 쓸 수 있는 값을 정의
    return render(request, 'dinner.html', {'menu':menu})
    # template 은 기본적으로 문법이 jinja2랑 비슷한데, 장고에서는 DTL을 쓴다.
    # Django Template Language