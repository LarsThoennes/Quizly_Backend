from django.urls import path
from .views import RegistrationView, CookieTokenObtainView, LogoutView, CookieRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CookieTokenObtainView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', CookieRefreshView.as_view(), name='token_refresh'),
]