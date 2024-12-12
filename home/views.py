from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"index.html")

def baidu(request):
    return render(request,"baidu.html")

def info(request):
    #1.普通的变量
    username = '管理员'
    #2.渲染一个字典类型
    book = {'name' : '水浒传','author' : '施耐庵'}
    #3.列表
    books = [
        {'name':'水浒传','author':'施耐庵'},
        {'name':'西游记','author':'吴承恩'},
        {'name':'三国演义','author':'罗贯中'},
    ]
    #4.对象
    class Person:
        def __init__(self,realname):
            self.realname = realname
    context = {
        'username': username,
        'book': book,
        'books': books,
        'person':Person("管理员7号")
    }
    return render(request,"info.html",context=context)

def if_view(request):
    age = 17
    return render(request,'if.html',context={'age':age})

def for_view(request):
    #1.列表
    books = [
        {'name': '水浒传', 'author': '施耐庵'},
        {'name': '西游记', 'author': '吴承恩'},
        {'name': '三国演义', 'author': '罗贯中'},
    ]
    #2.字典
    person = {
        'realname':"管理员七号",
        'age':21,
        'height':"180cm"
    }
    context = {
        'books':books,
        'person':person
    }
    return render(request,'for.html',context=context)

def with_view(request):
    context = {
        'books' : [
            {'name': '水浒传', 'author': '施耐庵'},
            {'name': '西游记', 'author': '吴承恩'},
            {'name': '三国演义', 'author': '罗贯中'},
        ]
    }
    return render(request,'with.html',context=context)

def url_view(request):
    return render(request,'url.html')

def book_detail(request,book_id):
    return HttpResponse(f"您访问的图书id：{book_id}")

def filter_view(request):
    greet = "hello world, hello django5"
    context = {
        'greet':greet,
        'birthday': datetime.now(),
        'profile':"我就是我，最亮的烟火",
        'profile1':"",
        'html':"<h1>欢迎来到武器库管理系统</h1>"
    }
    return render(request,'filter.html',context=context)

def template_form(request):
    context = {
        'articles':['小米su17发布','台湾统一']
    }
    return render(request,"xfz_index.html",context=context)

def static_view(request):
    return render(request,'static.html')

# views.py
from django.shortcuts import render, redirect

def toggle_view(request):
    if request.method == 'POST':
        selected_toggle = request.POST.get('toggle')
        if selected_toggle:
            # 根据 selected_toggle 的值执行不同的逻辑
            if selected_toggle == '1':
                return render(request, 'page1.html')
            elif selected_toggle == '2':
                return render(request, 'page2.html')
        else:
            # 如果没有选择任何选项，可以返回默认页面或提示用户选择
            return render(request, 'toggle_page.html')

    return render(request, 'toggle_page.html')