from django.shortcuts import render

from rest_framework import generics

from .models import Language, Education, Experience
from .serializers import LanguageSerializer, EducationSeriazlizer, ExperienceSerializer
# Create your views here.


class LanguageCreateListView(generics.CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
