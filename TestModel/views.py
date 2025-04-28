from django.shortcuts import HttpResponse
from django.shortcuts import render
from TestModel import models
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

from rest_framework.views import APIView
from rest_framework.response import Response
# from .models import User

# def add_book(request):
#     books = models.Book.objects.get(pk=5)
#     # books = models.Book.objects.get(pk=18)  # 报错，没有符合条件的对象
#     # books = models.Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
#     # print(books, type(books))  # 模型类的对象
#     return HttpResponse("<p>查找成功！</p>")

def add_book(request):
    book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    book.save()
    # models.Book.objects.create(title='sex')
    return HttpResponse("<p>数据添加成功！</p>")

def del_book(request):
    book = models.Book.objects.get(id=1).delete()
    # book.delete()
    print(book)
    return HttpResponse("<p>数据删除成功！</p>")

def sel_book(request):
    book = models.Book.objects.all()
    print(book)
    book = models.Book.objects.filter(pk=1)
    print(book)
    print(request)
    # book = models.Book.objects.aggregate(sum("id"))
    # print(book)
    return HttpResponse("<p>数据查询成功！</p>")

# def login(request):
#     list={"username": "123", "password": "123"}
#     # username=models.test3.username
#     # pwd=models.test3.pwd
#     return HttpResponse(request)

class LoginView(APIView):
    def post(self, request):
        usernamew = request.data.get('username')
        pwdw = request.data.get('password')
        # user = models.test3.objects.create(username="123", pwd="123")
        # user.save()

        # user = models.test3.objects.filter(pk=1).first()
        user = models.test3.objects.filter(username=usernamew,pwd=pwdw).first()
        if user == None:
            return Response({'code': 400, 'msg': "fail"})
        else:
            return Response({'code': 0, "username": usernamew, 'msg': "success"})


class index(APIView):
    def post(self, request):
        username = request.data.get("username")
        addr = request.data.get("addr")
        print(username)
        print(addr)
        data = models.Test.objects.create(name=username, test=addr)
        data.save()
        return Response({"code":200,"msg":"success"})





# def upd_book(request):
#     book = models.Book.delete(id(6))
#     book.delete()
#     return HttpResponse("<p>数据删除成功！</p>")

# def test(request):
#     Contest={};
#     Contest['hello']={"hello word"}
#     return render(request,r'https://www.runoob.com/django/django-template.html')



