"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from Books.views import *
# pkrefers to primary key or id
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',home , name='home_page' ),
    path('login/',loginPage , name='login_page'),
    path('register/',registerPage , name='register_page'),
    path('logout/',logoutUser , name='logout_page'),
    path('books/',booksPage , name='books_page'),
    path('get/book/<str:pk>/',get_book, name = 'get_book'),
    path('user/books/',userBooks, name = 'user_books'),
    path('return/book/<str:pk>/',return_book , name='return_book'),
    path('user/list/',userList , name='user_list'),
    path('delete/user/<str:pk>/',delete_user,name='delete_user'),
    path('update/user/<str:pk>/',update_user,name='update_user'),
    path('update/books/<str:pk>/',update_books,name='update_books'),



]
