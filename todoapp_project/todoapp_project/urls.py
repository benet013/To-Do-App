from django.contrib import admin
from django.urls import path, include
from user import views as user_view
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",user_view.register,name='register'),
    path("login/",user_view.CustomLoginView.as_view(template_name='user/login.html'),name='login'),
    path("logout/",user_view.CustomLogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path("", include('todolist.urls')),
]
