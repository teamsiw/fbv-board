from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 유효한 URL 패턴
]
