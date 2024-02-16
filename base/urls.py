from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('login.html', views.login_page, name='login_page_html'),
    path('main_student.html', views.main_student, name='main_student'),
]
