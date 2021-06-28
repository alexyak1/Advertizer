# from django.urls import path
# from rest_advert import views

# urlpatterns = [
#     path('ads/', views.ad_list),
#     path('ads/<int:pk>/', views.ad_detail),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_advert import views

urlpatterns = [
    path('ads/', views.AdList.as_view()),
    path('ads/<int:pk>/', views.AdDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)