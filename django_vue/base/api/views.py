from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import status, viewsets, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView

from django_vue.base.api.serializers import RegistrationSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django_vue.base.models import User


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response({"sucess": "csrf cookie set"})


@method_decorator(csrf_protect, name='dispatch')
class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            if request.user.is_authenticated:
                return Response({'status': 'isAuthenticated', 'first_name': request.user.first_name, 'email': request.user.email })
            else:
                return Response({'status': 'isNotAuthenticated'})
        except:
            return Response({'status': 'error', 'description': 'Something went wrong when checking authentication status.'})


@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email:
            return Response({'error': "'email' field is missing."})
        if not password:
            return Response({'error': "'password' field is missing."})
        if User.objects.filter(email=email).exists():
            return Response({'error': 'That email was already been registered.'})
        else:
            user = User.objects.create_user(email=email, password=password)
            user.save()
            return Response({"success": "user created successfully"})


@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    # def post(self, request, format=None):
    #     if request.user.is_authenticated:
    #         return {"status": "already_authenticated"}
    #     try:
    #     except:
    #         return Response({'error': 'Something went wrong when login user.'})

    def post(self, request, format=None):
        if request.user.is_authenticated:
            return Response({"status": "already_authenticated"})
        email = request.data.get('email')
        if not email:
            return Response({'error': "'email' field is missing."})

        password = request.data.get('password')
        if not password:
            return Response({'error': "'password' field is missing."})

        user = authenticate(username=email, password=password, request=request)
        if user is not None:
            login(request, user)
            # 'auth.login' will add user session in request, and in some way this session will be sent in Response
            # I think that APIView is doing this automatically.
            return Response({'first_name': request.user.first_name, 'email': request.user.email})
        else:
            return Response({"status": "login_failed"})


# if user is already logged with sessionAuthentication, the views will be CSRF protected. You just need to use the CSRF
# decorator if you use 'permission.AllowAll'
class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            logout(request)
            return Response({'success': 'Loggout out'})
        except:
            return Response({'error': 'Something went wrong when logging out.'})


class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        request.user.delete()
        return Response({"success": "User deleted successfully."})


@api_view(['GET', ])
# @authentication_classes([])
# @permission_classes([AllowAny])
def test_view(request):
    data = {'some': 'Data'}
    return Response(data)
