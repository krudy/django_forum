"""
URL configuration for forum_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from forum import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('category/<int:category_id>/', views.category_threads, name='category_threads'),
    path('thread/new/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/reply/', views.add_reply, name='add_reply'),
]
