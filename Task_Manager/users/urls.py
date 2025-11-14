from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView, 
    TokenBlacklistView,
)
from .authentication import jwt_views

urlpatterns = [
    path('api/token/', jwt_views.LogInTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tokeerify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/logout/', jwt_views.LogOutView.as_view(), name='token_blacklist'),
]