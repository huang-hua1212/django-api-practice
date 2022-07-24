from django.contrib import admin
from django.urls import path,include
# from .views import ListView
from .views import data1View
from .views import data2View

from datas import views


 
urlpatterns = [
    # path('data1/', data1View.as_view(),name='data1'),
    # path('data2/', data2View.as_view(), name='data2')

    path('rooms/', views.getRooms,name='rooms'),
    path('posts/', views.getPosts,name='posts'),
    path('users/', views.getUsers,name='users'),
    path('followings/', views.getFollowings,name='followings'),


    path('data2/', views.getData2, name='data2')
]