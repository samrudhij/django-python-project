"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.display),
    path('h/', views.receive,name='hlp'),
    path('rcv/', views.doLogin,name='register'),
    path('feed/', views.feedback,name='feed'),
    path('rpt1/',views.showfeedback),
    path('rpt2/',views.showlogin),
    path('rpt3/',views.showhelp),
    path('rpt4/',views.showorder),
    path('rpt5/',views.showproduct),
    path('test/cnc/',views.docancel),
    path('test/p/',views.mypaneer),
    path('p1/',views.paneer,name='pro1'),
    path('test/p2/',views.mydosa),
    path('test/p3/',views.myidli),
    path('test/p4/',views.mymanchurian),

]
