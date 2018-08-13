from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Language

def index(request):
    return HttpResponse("编程语言热度排行榜")

def my_html1(req):
    return render(req, "my_index1.html")

def get_data1(req):
    #获取数据
    data = Language.objects.all()
    print(data)
    return render(req, "my_index1.html",context={"my_data1":data})