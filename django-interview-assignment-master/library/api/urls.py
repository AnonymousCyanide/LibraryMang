from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('all/book/data/',views.get_Data),
    path('add/book/',views.add_book),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair' ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    
]