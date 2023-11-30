from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CompanyProfile, JobSearcherProfile
from common.serializers import EducationSeriazlizer, LanguageSerializer, ExperienceSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['phone_number'] = user.phone_number
        return token


class CompanyRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CompanyProfile.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CompanyProfile
        fields = (
            'phone_number',
            'email',
            'title',
            'legal_name',
            'activity',
            'district',
            'password',
            'password2',
        )
        extra_kwargs = {
            'title': {'required': True},
            'legal_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        company = CompanyProfile.objects.create(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            title=validated_data['title'],
            legal_name=validated_data['legal_name'],
            district=validated_data['district']
        )
        for activity in validated_data['activity']:
            company.activity.add(activity)

        company.set_password(validated_data['password'])
        company.save()

        return company


class JobSearcherProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CompanyProfile.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = JobSearcherProfile
        fields = (
            'phone_number',
            'email',
            'full_name',
            'gender',
            'bithed_date',
            'about',
            'salary',
            'currency',
            'is_freelancer',
            'district',
            'activity',
            'skills',
            'driver_license',
            # 'educations',
            # 'languages',
            # 'experiences',
            'password',
            'password2',
        )
        extra_kwargs = {
            'full_name': {'required': True},
            'legal_name': {'required': True},
            'full_name': {'required': True},
            'gender': {'required': True},
            'bithed_date': {'required': True},
            'about': {'required': True},
            'salary': {'required': True},
            'currency': {'required': True},
            'district': {'required': True},
            'activity': {'required': True},
            'skills': {'required': True},
            'driver_license': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        job_searcher = JobSearcherProfile.objects.create(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            gender=validated_data['gender'],
            bithed_date=validated_data['bithed_date'],
            about=validated_data['about'],
            salary=validated_data['salary'],
            currency=validated_data['currency'],
            is_freelancer=validated_data['is_freelancer'],
            district=validated_data['district'],
            activity=validated_data['activity'],
            skills=validated_data['skills'],
            driver_license=validated_data['driver_license'],
        )

        job_searcher.set_password(validated_data['password'])
        job_searcher.save()

        return job_searcher
