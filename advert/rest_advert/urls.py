from django.urls import path
from rest_advert import views

urlpatterns = [
    path('ads/', views.ad_list),
    path('ads/<int:pk>/', views.ad_detail),
]