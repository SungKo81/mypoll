"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('account/', include('account.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # http:/127.0.0.1:8000/
]

#### 파일 업로드 관련 설정. MEDIA_ROOT의 url로 요청이 들어오면 받을수 있도록 설정. 
#    (개발서버 -runserver에서 필요) 
from django.conf.urls.static import static 
from . import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# TemplateView
## 요청을 받으면 단순히 template을 응답하는 View를 만들 경우 사용.
## - template 파일의 경로만 지정.