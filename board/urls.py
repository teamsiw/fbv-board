from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),  # 유효한 URL 패턴
    path('list/', views.list, name='list'),
    path('read/<int:id>', views.read, name='read'),
]
