장고
1. 프로젝트 생성
    1. project 디렉토리
        mkdir mypoll 
        cd my poll

    2. 프로젝트 생성
        django-admin startproject config . 
        python manage.py runserver 

2. 앱 생성
    1. mypoll > python manage.py startapp polls
        - polls: 앱 이름

    2. 생성한 앱을 프로젝트에 등록
        - config/setting.py
            - INSTALLED_APP에 polls를 등록
        - settings.py에 추가 설정
            - LANGUAGE_CODE = 'ko-kr'
            -TIME_ZONE = 'Asia/Seoul'
        - config/urls.py
        - 파일생성 - polls/urls.py

3. 관리자(superuser) 계정 생성 (터미널)
    - mypoll > python manage.py migrate 
    - mypoll > python manage.py createsuperuser
        - 사용자 이름 : username (root)
        - 이메일 : a@a.com
        - password: 1111
    - python manage.py runserver 
        - http://127.0.0.1:8000/admin

4. Model 정의
    1. Model 클래스 정의 (polls/models.py)
    2. admin.py에 모델 클래스 등록 
    3. python manage.py makemigrations 
        - DB에 테이블을 생성/수정할 코드를 생성. 
    4. python manage.py migrate
        - DB에 테이블을 생성/수정 한다. 
    - python manage.py runserver

# static 파일
- join.jpg
    - account/static/account

## static 파일을 찾는 순서 
1. settings.STATICFILES_DIRS 경로
2. APP/static
    - app은 INSTALLED APP에 등록된 순서대로 찾는다. 

# media
- 파일 업로드 관련 설정.

## settings.py
MEDIA_URL: 업로드된 파일을 사용자가 요청할떄 사용할 시작 PATH
MEDIA_ROOT: 업로드된 파일들을 저장할 디렉토리 경로.(파일경로)