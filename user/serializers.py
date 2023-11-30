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
        # extra_kwargs = {
        #     'title': {'required': True},
        #     'legal_name': {'required': True}
        # }

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

    # def create(self, validated_data):
    #     job_searcher = JobSearcherProfile.objects.create(
    #         phone_number=validated_data['phone_number'],
    #         email=validated_data['email'],
    #         full_name=validated_data['full_name'],
    #         gender=validated_data['gender'],
    #         bithed_date=validated_data['bithed_date'],
    #         about=validated_data['about'],
    #         salary=validated_data['salary'],
    #         currency=validated_data['currency'],
    #         is_freelancer=validated_data['is_freelancer'],
    #         district=validated_data['district'],
    #         activity=validated_data['activity'],
    #         # skills=validated_data['skills'],
    #     )

    #     for driver_licence in validated_data['driver_license']:
    #         job_searcher.driver_license.add(driver_licence)

    #     for skill in validated_data['skills']:
    #         job_searcher.skills.add(skill)

    #     job_searcher.set_password(validated_data['password'])
    #     job_searcher.save()

    #     return job_searcher


class JobSearcherVerifySerailizer(serializers.Serializer):
    phone_number = serializers.CharField()
    session = serializers.CharField()
    code = serializers.CharField()
