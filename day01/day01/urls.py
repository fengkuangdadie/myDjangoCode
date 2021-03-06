"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from t01.views import index,my_html,get_data
from ProgrammingLanguage.views import index,my_html1,get_data1

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^hello$",index),
    url(r"^index/",my_html),
    url(r"^get-data/",get_data),
    url(r"^get-data1/",get_data1)
]
