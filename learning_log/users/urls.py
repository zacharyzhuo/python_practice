"""Defines URL patterns for users."""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
# 句點是讓Python從目前的urls.py模組所在的資料夾匯入視窗

app_name = "users"  # 必須加上

urlpatterns = [
    # r''為原始字串，^$分別查看字串頭尾
    # 第二引數指定要呼叫的視窗函式
    # 第三引數把這個URL模式的名稱指定為index

    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register, name='register'),
]
