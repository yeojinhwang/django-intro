# Django

1. MVC(Model View Controller)

- Model: Database와 유사한 개념
- View: html 보여주는 것과 관련된 개념
- Controller: Model과 View 사이의 연결고리 역할을 함

1. django에서는 MTV: Template은 View, View는 Controller와 동일한 역할



## 1. 시작하기

1. 프로젝트 시작하기

```bash
$ django-admin startproject 프로젝트이름
```

아래와 같이 프로젝트 구조가 만들어진다.

```
├── db.sqlite3
├── django_intro
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

지금부터 pwd는 `~/workspace/django_intro`이다.

1. 서버 실행하기

   - settings.py

   ```python
   ALLOWED_HOSTS = ['*']
   # c9에서는 host - 0.0.0.0, port - 8080만 활용할 수 있기 때문에 위와 같이 설정한다.
   ```

```bash
~/workspace/django_intro $ python manage.py runserver 0.0.0.0:8080
```

앞으로 모든 장고 명령어는 프로젝트를 만들 때를 제외하고, `python manage.py`를 활용한다.

따라서, 명령어가 안될 때에는 반드시 `pwd`와 `ls`를 통해 현재 bash(터미널) 위치를 확인하자!!

1. 앱 만들기

```bash
$ python manage.py startapp 앱이름
```



## 2. Hello, Django!

> Django 프로젝트는 여러가지 app의 집합이다.
>
> 각각의 app은 MTV 패턴으로 구성되어 있다.
>
> M (Model) : 애플리케이션 핵심 로직의 동작을 수행한다.
>
> T (Template) : 사용자에게 결과물을 보여준다.
>
> V (View) : 모델과 템플릿의 동작을 제어한다. (모델의 상태를 변경하거나 값을 가져오고, 템플릿에 값을 전달하기 등)
>
> **일반적으로 MVC패턴으로 더 많이 사용된다.**

### 1) 기본 로직

앞으로 우리는 1. 요청 url 설정(`urls.py`) 2. 처리할 view 설정(`views.py`) 3. 결과 보여줄 template 설정(`templates/`)으로 작성할 것이다.

1. url 설정

   ```python
   # django_intro/urls.py
   from django.contrib import admin
   from django.urls import path
   # home 폴더 내에 있는 views.py를 불러온다.
   from home import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       # 요청이 home/을 오면, views의 index 함수를 실행시킨다.
       path('home/', views.index)
   ]
   ```

2. view 설정

   ```python
   # home/views.py
   from django.shortcuts import render, HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpResponse('hello, django!')
   ```

   - 주의할 점은 선언된 함수에서 `request`를 인자로 받아야 한다.
     - request는 사용자(클라이언트)의 요청 정보와 서버에 대한 정보가 담겨 있다.
     - Django 내부에서 해당 함수를 호출하면서 정보를 넘겨주기 때문에 반드시 명시해줘야 한다.

## 3. Template (MTV-T)

> Django에서 활용되는 Template은 DTL(Django Template Language)이다.
>
> jinja2와 문법이 유사하다.

1. url 설정

   ```python
   path('home/dinner/', views.dinner)
   ```

2. view 설정

   ```python
   def dinner(request):
       box = ['chicken', 'pasta', 'pizza', 'hamburger', 'sushi', 'pho']
       menu = random.choice(box)
       return render(request, 'dinner.html', {'menu':menu})
   ```

   - Template을 리턴하려면 `render`를 사용하여야 한다.
     - `request`(필수)
     - `template 파일이름`(필수)
     - `template 변수`(선택):`dictionary` 타입으로 구성해야 한다.

3. Template 설정

   ```bash
   $ mkdir home/templates
   $ touch home/templates/dinner.html
   ```

   ```django
   <!--home/templates/dinner.html-->
   <h1> {{menu}} </h1>
   ```

![Image from iOS](image/Image from iOS.jpg)



## 4. Variable Routing

1. url 설정

   ```python
   path('home/you/<name>/', views.you),
   path('home/cube/<int:num>/', views.cube)
   ```

2. view 파일 설정

   ```python
   def you(request, you):
       return render(request, 'you.html', {'name':name})
   ```

3. 템플릿 파일 설정

   ```django
   <h1> {{ name }}, 안녕!! </h1>
   ```



## 5. Form data

1. `ping`

   1) 요청 url 설정

   ```python
   path('home/ping/', views.ping)
   ```

   2) view 설정

   ```python
   def ping(request):
       return render(request, 'ping.html')
   ```

   3) template 설정

   ```django
   <form action="/home/pong/">
       <input type="text" name="message">
       <input type="submit">
   </form>
   ```

2. `pong`

   1) 요청 url 설정

   ```python
   path('/home/pong/', views.pong)
   ```

   2) view 설정

   ```python
   def pong(request):
       msg = request.GET.get('message')
       return render(request, 'pong.html', {'msg':msg})
   ```

   3) template 설정

   ```django
   <h1>{{ msg }}</h1>
   ```

3. POST 요청 처리

   1) 요청 FORM 수정

   ```django
   <form action="/home/pong" method="POST">
       {% csrf_token %}
   </form>
   ```

   2) view 수정

   ```python
   def pong(request):
       message = request.POST.get('message')
   ```

   - `csrf_token`은 보안을 위해 django에서 기본적으로 설정되어 있는 것이다.
     - CSRF 공격: Cross Sites Request Forgery
     - form을 통해 POST 요청을 보낸다는 것은 데이터베이스에 반영되는 경우가 대부분인데, 해당 요청을 우리가 만든 정해진 form에서 보내는지 검증하는 것이다.
     - 실제로 input type hidden으로 특정한 hash 값이 담겨 있는 것을 볼 수 있다.
     - `settings.py`에 `MIDDLEWARE` 설정을 보면 csrf 관련된 내용이 설정된 것을 볼 수 있다.

## 6. static file 관리

> 정적 파일(images, css, js)을 서버 저장이 되어 있을 때, 이를 각각의 템플릿에 불러오는 방법

### 디렉토리 구조

디렉토리 구조는 `home/static/home/` 으로 구성된다.

이 디렉토리 설정은 `settings.py` 의 가장 하단에 `STATIC_URL` 에 맞춰서 해야한다. (기본 `/static/`)

1.  파일 생성

   `home/static/home/images/iu.jpg` 

   `home/static/home/stylesheets/style.css`

2. 템플릿 활용

   ```django
   {% extends 'base.html' %}
   {% load static %}
   {% block css %}
   <link rel="stylesheets" type="text/css" href="{% static 'home/stylesheets/style.css' %}"
   {% endblock %}
   {% block body %}
   <img src="{% static 'home/images/iu.jpg' %}">      
   {% endblock %}
   ```

   > {% extends file %}은 무조건 가장 상단에 위치해야 함

## 7. URL 설정 분리

> 위와 같이 코드를 짜는 경우에, `django_intro/urls.py` 에 모든 url 정보가 담기게 된다.
>
> 일반적으로 Django 어플리케이션에서 url을 설정하는 방법은 app 별로 `urls.py` 를 구성하는 것이다. 

1. `django_intro/urls.py`

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('home/', include('home.urls')),
   ]
   ```

   - `include` 를 통해 `app/urls.py` 에 설정된 url을 포함한다.

2. `home/urls.py`

   ```python
   from django.urls import path
   # views는 home/views.py
   from . import views
   
   urlpatterns = [
       path('', views.index),
   ]
   ```

   - `home/views.py` 파일에서 `index`를 호출하는 url은 `http://<host>/` 이 아니라, `http://<host>/home/` 이다.

## 8. Template 폴더 설정

### 디렉토리 구조

디렉토리 구조는 `home/templates/home/` 으로 구성된다.

디렉토리 설정은 `settings.py` 의 `TEMPLATES` 에 다음과 같이 되어 있다.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'django_intro', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- `DIRS` : templates를 커스텀하여 경로를 설정할 수 있다.

  - 경로 설정

    ```python
    os.path.join(BASE_DIR, 'django-intro', 'templates')
    #=> django_intro/django_intro/templates/
    ```

- `APP_DIRS` : `INSTALLED_APPS` 에 설정된 app의 디렉토리에 있는 `templates` 를 템플릿으로 활용한다. (TRUE)

1. 활용 예시

   ```python
   # home/views.py
   def index(request):
       return render(request, 'home/index.html')
   ```

   ```
   home
   ├── __init__.py
   ├── admin.py
   ├── apps.py
   ├── migrations
   ├── models.py
   ├── templates
   │   └── utilities
   │       └── index.html
   ├── tests.py
   ├── urls.py
   └── views.py
   ```










# Django day 2

DTL(Django Template Language)에서는 dictionary value를 가져올 때 dictionary[key]가 아닌 dictionary.key형태로 가져온다.

> framework 공통적인 사항
>
> I18N: 국제화/지역화
>
> L10N
>
> TZ

### Built-in template tags and filters

1. for

   https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#for

2. if

   https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#if

1. date

   https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#date

```django
<p>1. 반복문</p>
{% for menu in my_list %}
    {{ forloop.counter }}
    {% if forloop.first %}
        <p>짜장며어어언</p>
    {% else %}
        <p>{{ menu }}</p>
    {% endif %}
{% endfor %}
{% for user in empty_list %}
    <p>{{ user }}</p>
    {% empty %}
        <p>지금 가입된 유저가 없습니다.</p>
{% endfor %}
<hr>
<p>2. 조건문</p>
{% if '치킨' in my_list %}
    <p>짜장면은 고춧가루 없이 못 먹지!</p>
{% endif %}
<hr>
<p>3. length filter 활용</p>
{% for message in messages %}
    {% if message|length > 5 %}
        <p>글씨가 너무 길어요</p>
    {% else %}
        <p>{{ message }}, {{ message|length }}</p>
    {% endif %}
{% endfor %}
<hr>
<p>4. lorem ipsum : % 주의하자!</p>
{% lorem %}
<hr>
{% lorem 3 w %}
<hr>
{% lorem 4 w random %}
<hr>
{% lorem 4 p %}
<hr>
<p>5. 글자수 제한하기(truncate)</p>
<p>{{ my_sentence|truncatewords:3 }}</p>
<p>{{ my_sentence|truncatechars:10 }}</p>
<hr>
<p>6. 글자 관련 필터</p>
<p>{{ 'abc'|length }}</p>
<p>{{ 'ABC'|lower }}</p>
<h3>{{ my_sentence|title }}</h3>
<p>{{ 'abc def'|capfirst }}</p>
<p>{{ my_list|random }}</p>
<hr>
<p>7. 연산 - django-mathfilters 쓰면 추가적으로도 가능하긴함.</p>
<p>{{ 4|add:6 }}</p>
<hr>
<p>8. 날짜표현</p>
{{ now }}
{% now "SHORT_DATETIME_FORMAT" %} <br>
{% now "TIME_FORMAT" %} <br>
{% now "SHORT_DATE_FORMAT" %} <br>
{% now "DATE_FORMAT %} <br>
{% now "Y년 m월 d일 (l) h:i" %} <br>
<hr>
{{ datetimenow|date:"SHORT_DATE_FORMAT" }} <br>
{{ 'https://google.com'|urlize }}
```

