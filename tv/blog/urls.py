from django.conf.urls import url
from django.contrib import admin 
from django.urls import path ,include
from .views import  blog_Cntnt
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.blog_Cntnt, name='blog_Cntnt'),
    path('<str:cntnt_slug>/', views.blog_Cntnt, name='details'),
    path('pp/<str:blog_cntnt_dtls>/', views.blog_Cntnt, name='sub_details'),
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<str:slug>/', views.product_detail, name='sub_product_list'),
]
