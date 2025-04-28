"""
URL configuration for djangoProj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from TestModel import views
from TestModel.apps import TestmodelConfig
from TestModel.views import LoginView,index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_book/', views.add_book),
    path('del_book/', views.del_book),
    path('sel_book/', views.sel_book),
    path('login/', LoginView.as_view()),  #wxapp
    path('index/', index.as_view()),  # wxapp

    # path('test/',views.test)
    # path('TestmodelConfig/', ),
]
# from django.contrib import admin
# from django.urls import path
# from TestModel2 import views
# urlpatterns = {
#     path('admin/', admin.site.urls),
#     path('SmsCodeView/', views.SmsCodeView),
#     path('RegisterView/', views.RegisterView),
#
# }


