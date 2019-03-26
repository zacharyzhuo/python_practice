"""Defines URL patterns for learning_logs.

learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from . import views
# 句點是讓Python從目前的urls.py模組所在的資料夾匯入視窗

app_name = "learning_logs" # 必須加上

urlpatterns = [
    # r''為原始字串，^$分別查看字串頭尾
    # 第二引數指定要呼叫的視窗函式
    # 第三引數把這個URL模式的名稱指定為index

    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path('new_entry<int:topic_id>/', views.new_entry, name='new_entry'),
]