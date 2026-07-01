from rest_framework import serializers
from .models import CustomUser


class PatientRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'password', 'phone']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['email'],  # using email as username
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            phone=validated_data.get('phone', ''),
            role='patient'  # automatically set role as patient
        )
        return user


class DoctorRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'name', 'email', 'password',
            'specialty', 'license_number', 'license_document_url'
        ]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['email'],  # using email as username
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            specialty=validated_data.get('specialty', ''),
            license_number=validated_data.get('license_number', ''),
            license_document_url=validated_data.get('license_document_url', ''),
            role='doctor',  # automatically set role as doctor
            verification_status='pending'  # always starts as pending
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    