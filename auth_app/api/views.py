from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegistrationSerializer, CustomTokenObtainSerializer
from rest_framework import status

class RegistrationView(APIView):
    """
    Handles user registration by creating a new user account.

    - Public endpoint (no authentication required)
    - Validates input data using RegistrationSerializer
    - Creates a new user and returns a success message
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            data = {
                'username': saved_account.username,
                'email': saved_account.email,
                'user_id': saved_account.pk
            }
            return Response({"detail": "User created successfully!"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CookieTokenObtainView(TokenObtainPairView):
    """
    Authenticates a user and issues JWT access and refresh tokens.

    - Public endpoint (no authentication required)
    - Generates access and refresh tokens using JWT
    - Stores tokens securely in HTTP-only cookies
    - Returns user information after successful login
    """
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access = serializer.validated_data["access"]
        refresh = serializer.validated_data["refresh"]

        user = serializer.user 

        response = Response(
            {
                "detail": "Login successfully!",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            },
            status=status.HTTP_200_OK
        )

        response.set_cookie(
            key='access_token',
            value=str(access),
            httponly=True,
            secure=False,
            samesite='Lax',
        )

        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=False,
            samesite='Lax',
        )

        return response

class LogoutView(APIView):
    """
    Logs out the authenticated user by deleting JWT tokens from cookies.

    - Requires authentication
    - Removes access and refresh tokens from the client
    - Invalidates the session on the client side
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response(
            {"detail": "Log-Out successfully! All Tokens will be deleted. Refresh token is now invalid."},
            status=status.HTTP_200_OK
        )

        response.delete_cookie(
            key="access_token",
            path="/",
        )

        response.delete_cookie(
            key="refresh_token",
            path="/",
        )

        return response

class CookieRefreshView(TokenRefreshView):
    """
    Refreshes the JWT access token using the refresh token stored in cookies.

    - Reads refresh token from HTTP-only cookies
    - Issues a new access token if the refresh token is valid
    - Returns an error if the refresh token is missing or invalid
    """
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')

        if refresh_token is None:
            return Response({'error': 'No refresh token provided in cookies'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={'refresh': refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({'error': 'Refresh Token invalid'}, status=status.HTTP_401_UNAUTHORIZED)
        
        access_token = serializer.validated_data.get('access')

        response = Response({'detail': 'Token refreshed', 'access': access_token}, status=status.HTTP_200_OK)
        
        response.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=False,
            samesite='Lax',
        )

        return response