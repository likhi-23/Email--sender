from django.contrib import admin
from django.urls import path,include
from emailsend import views
urlpatterns = [
     path('',views.index, name='index'),
    path('mail',views.send,name='mail')
] 
