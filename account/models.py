from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import forms

## 확장 User 모델
# - AbstractUser로 구현 : 기본 User(username, password)에 필드들을 추가하는 방식
# - AbstractUser 상속. 필드들 정의(username, password 빼고 정의)
class User(AbstractUser):
    # Field 들 정의 - table 컬럼
    name = models.CharField(
        verbose_name='이름', # form 관련 설정 (label) - Form을 ModelForm을 만들 경우 form 관련 설정을 Model에 한다.
        max_length=50, # varchar(50)
    )
    email = models.EmailField(
        verbose_name='이메일',
        max_length=100, # EmailField: varchar(100) -> 값이 이메일 형식인지 (@가 있는지)를 검증. 
    )
    birthday = models.DateField(
        verbose_name='생일',
        null=True, # Null 허용 (default: False - Not Null),
        blank=True # Form 설정 - 필수가 아니다. (default: False - required)
    )
    profile_img = models.ImageField(
        verbose_name='프로필 사진',
        upload_to='images/%Y/%m/%d', # 저장 경로 (media/지정한 경로)
        null=True,
        blank=True
    ) # 추가 -> makemigrations, migrate 
    
