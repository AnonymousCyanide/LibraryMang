from django.urls import path
from . import views
urlpatterns = [
    path('alldata/',views.get_Data),
    path('addbook/',views.add_book)
    
]