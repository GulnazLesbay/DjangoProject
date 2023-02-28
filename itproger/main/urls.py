from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about, name="about"),
    path('home', views.index, name="index"),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('main/<slug:category_slug>/', views.category_list, name='category_list'),
]
