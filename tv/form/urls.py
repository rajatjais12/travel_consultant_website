from django.conf.urls import url
from django.contrib import admin 
from django.urls import path ,include
from .views import  log_in
from . import views
from django.contrib.auth import views as auth_views

app_name = 'form'


urlpatterns = [
    #path('', views.log_in, name='log_in'),
    path('',views.log_in, name='log_in'),

    #path('<str:cntnt_slug>/', views.blog_Cntnt, name='details'),
    #path('pp/<str:blog_cntnt_dtls>/', views.blog_Cntnt, name='sub_details'),
    #path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<str:slug>/', views.product_detail, name='sub_product_list'),
]
