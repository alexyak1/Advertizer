from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_advert import views

urlpatterns = [
    path('ads/', views.AdList.as_view(), name='AdList'),
    path('ads/<int:pk>/', views.AdDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)