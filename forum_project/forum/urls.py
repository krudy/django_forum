from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('category/<int:category_id>/', views.category_threads, name='category_threads'),
    path('thread/new/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/reply/', views.add_reply, name='add_reply'),
]
