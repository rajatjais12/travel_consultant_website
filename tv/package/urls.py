from django.conf.urls import url
from django.contrib import admin 
from django.urls import path ,include
from .views import  product_list
from . import views

app_name = 'package'


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('detail/<int:id>/<str:slug>/', views.product_detail, name='sub_product_list'),
    path('category_them/<str:them_slug>', views.product_list, name='theme_product_list'),
    path('category_price/<str:price_slug>', views.product_list, name='price_product_list'),
    path('category_offer/<str:offer_slug>', views.product_list, name='offer_product_list'),
    path('category_destination/<str:cat_slug>', views.product_list, name='cat'),
]



    # path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    # path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='sub_product_list'),