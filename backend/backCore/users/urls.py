from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from users.token import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import UserViewSet, UserCreateViewSet, UserLookupView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

urlpatterns = [
    
    path('register/', UserCreateViewSet.as_view({'post': 'create'}), name='user-create'),
    path('users/', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('lookup/', UserLookupView.as_view(), name='user-lookup'),
]
