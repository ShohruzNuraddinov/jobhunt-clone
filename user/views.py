from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from .serializers import MyTokenObtainPairSerializer, CompanyRegisterSerializer, JobSearcherProfileSerializer
from .models import CompanyProfile, JobSearcherProfile


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CompanyRegisterView(generics.CreateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyRegisterSerializer
    # permission_classes


class JobSearcherRegisterView(generics.CreateAPIView):
    queryset = JobSearcherProfile
    serializer_class = JobSearcherProfileSerializer
