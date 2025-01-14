from django.contrib import admin
from .models import Question, Choice
# .models -> 상대경로로 import. admin.py와 같은 패키지에 있는 models.py 
# Register your models here. -> admin app에서 데이터를 관리할수 있도록 등록


admin.site.register(Question)
admin.site.register(Choice)


