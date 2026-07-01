from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import PatientRegisterSerializer, DoctorRegisterSerializer


# Helper function to generate JWT token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


class PatientRegisterView(APIView):

    def post(self, request):
        serializer = PatientRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'token': token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorRegisterView(APIView):

    def post(self, request):
        serializer = DoctorRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                'id': user.id,
                'name': user.name,
                'verification_status': user.verification_status,
                'token': token
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientLoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # find user by email
        try:
            user = CustomUser.objects.get(email=email, role='patient')
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Invalid email or password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check password
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response(
                {'error': 'Invalid email or password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token = get_tokens_for_user(user)
        return Response({
            'id': user.id,
            'name': user.name,
            'token': token
        }, status=status.HTTP_200_OK)


class DoctorLoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # find user by email
        try:
            user = CustomUser.objects.get(email=email, role='doctor')
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Invalid email or password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check password
        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response(
                {'error': 'Invalid email or password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token = get_tokens_for_user(user)
        return Response({
            'id': user.id,
            'name': user.name,
            'verification_status': user.verification_status,
            'token': token
        }, status=status.HTTP_200_OK)
        