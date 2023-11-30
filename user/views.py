import json
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _

from user.serializers import MyTokenObtainPairSerializer, CompanyRegisterSerializer, JobSearcherProfileSerializer, CompanyRegisterVerifySerailizer, JobSearcherVerifySerailizer
from user.models import CompanyProfile, JobSearcherProfile
from user.generators import sms_code_generate, session_token_generate


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CompanyRegisterView(generics.GenericAPIView):
    # queryset = CompanyProfile.objects.all()
    serializer_class = CompanyRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        session = session_token_generate()
        code = sms_code_generate()
        print(code)

        phone_number = data['phone_number']

        if cache.get(phone_number, None) is not None:
            return Response(
                {
                    'message': _("Phone NUmber already sent sms code.")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        auth_data = {
            'session': session,
            'code': code
        }

        cache.set(phone_number, auth_data, 120)
        cache.set(session, data, 300)
        cache.get(phone_number)
        data = {
            'title': data['title'],
            'phone_number': data['phone_number'],
            'session': session
        }
        # data.update({'session': session})

        return Response(data=data, status=status.HTTP_200_OK)


class CompanyRegisterVerify(generics.GenericAPIView):
    serializer_class = CompanyRegisterVerifySerailizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        session = data['session']
        phone_number = data['phone_number']
        code = data['code']

        cache_data = cache.get(phone_number, None)

        if cache_data is None:
            return Response(
                data={
                    "error": _("Verification code is expired. Or invalid phone entered!")
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if cache_data['code'] != code:
            return Response(
                {
                    'message': _("Incorrect Code!")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        all_data = cache.get(session, None)
        try:
            company = CompanyProfile(**all_data)
            company.save()
            data.update({'success': True})
            return Response(data=data, status=status.HTTP_201_CREATED)
        except:
            data = {
                'message': "Already created Phone Number",
                'success': False
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class JobSearcherRegisterView(generics.GenericAPIView):
    serializer_class = JobSearcherProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        code = sms_code_generate()
        session = session_token_generate()
        print(code)

        phone_number = data['phone_number']
        full_name = data['full_name']

        if cache.get(phone_number, None) is not None:
            return Response(
                {
                    'message': _("This Phone number already sent sms code.")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        auth_data = {
            'session': session,
            'code': code
        }
        cache.set(phone_number, auth_data, 120)
        cache.set(session, data, 300)
        data = {
            'phone_number': phone_number,
            'full_name': full_name,
            'session': session
        }

        return Response(data)


class JobSearcherVerifyView(generics.GenericAPIView):
    serializer_class = JobSearcherVerifySerailizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        phone_number = data['phone_number']
        session = data['session']
        code = data['code']

        auth_data = cache.get(phone_number, None)

        if auth_data is None:
            return Response(
                {
                    'message': _('Verification code is expired. Or invalid phone entered!')
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if auth_data['code'] != code:
            return Response(
                {
                    'message': _('Incorrect code!')
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        all_data = cache.get(session)

        try:
            job_searcher = JobSearcherProfile(**all_data)
            job_searcher.save()
            data = {
                'message': _("Successfully created"),
                'success': True,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except:
            data = {
                'message': _("Already created Phone Number"),
                'success': False
            }
            return Response(data, status=status.HTTP_201_CREATED)
