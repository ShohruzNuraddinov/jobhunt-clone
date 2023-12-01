from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils.translation import gettext_lazy as _

from .models import CompanyProfile, JobSearcherProfile
from common.serializers import EducationSeriazlizer, LanguageSerializer, ExperienceSerializer, SocialMediaSerailzier


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['phone_number'] = user.phone_number
        return token


class CompanyRegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CompanyProfile.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = CompanyProfile
        fields = (
            'phone_number',
            'email',
            'title',
            'legal_name',
            # 'activity',
            # 'district',
            'password',
        )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number', None)

        if phone_number is not None:
            if CompanyProfile.is_phone_number_available(phone_number=phone_number):
                raise serializers.ValidationError(
                    {"phone_number": _("This number is already taken")}
                )

        return attrs


class CompanyRegisterVerifySerailizer(serializers.Serializer):
    phone_number = serializers.CharField()
    session = serializers.CharField()
    code = serializers.CharField()


class JobSearcherProfileSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=JobSearcherProfile.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    # educations = EducationSeriazlizer()
    # languages = LanguageSerializer()
    # experiences = ExperienceSerializer()
    # social_medias = SocialMediaSerailzier()

    class Meta:
        model = JobSearcherProfile
        fields = (
            'phone_number',
            'password',
            'email',
            'full_name',
            'gender',
            'bithed_date',
            'about',
            'salary',
            'currency',
            'is_freelancer',
            # -------- Relation
            # 'district',
            # 'activity',
            # 'skills',
            # 'driver_license',

            # -------- Other Fields
            # 'educations',
            # 'languages',
            # 'experiences',
            # 'social_medias'

        )

    def validate(self, attrs):
        phone_number = attrs['phone_number']

        if phone_number is not None:
            if JobSearcherProfile.is_phone_number_available(phone_number=phone_number):
                raise serializers.ValidationError(
                    {
                        'message': "This Phone Number already taken!"
                    }
                )

        return attrs


class JobSearcherVerifySerailizer(serializers.Serializer):
    phone_number = serializers.CharField()
    session = serializers.CharField()
    code = serializers.CharField()
