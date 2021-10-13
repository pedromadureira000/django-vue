from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from django_vue.base.api.views import (
    test_view, SignupView, LoginView, LogoutView, CheckAuthenticatedView, GetCSRFToken, DeleteAccountView,
)

app_name = 'base'
urlpatterns = [
    path('register', SignupView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('checkauth', CheckAuthenticatedView.as_view(), name='checkauth'),
    path('getcsrf', GetCSRFToken.as_view(), name='getcsrf'),
    path('gettoken', obtain_auth_token, name='gettoken'),
    path('delete', DeleteAccountView.as_view(), name='deleteAccount'),
    path('test', test_view, name='teste'),
]
