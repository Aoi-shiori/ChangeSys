"""ChangeSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse
from change_management import views
from django.urls import  converters

def index(request):
    return HttpResponse('这是我的第一个首页')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",index),
    path("change_management/", include('change_management.urls',namespace='change_management')),
    # path("change_management1/", include('change_management.urls',namespace='change_management1')),
    # path("change_management2/", include('change_management.urls','change_management')),

]
