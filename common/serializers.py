from rest_framework import serializers

from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            'id',
            'user',
            'language',
            'degree'
        ]


class EducationSeriazlizer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'id',
            'title',
            'level',
            'direction',
            'begin_month',
            'begin_year',
            'finish_month',
            'finish_year',
            'about',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id',
            'title',
            'company_name',
            'begin_month',
            'begin_year',
            'finish_month',
            'finish_year',
            'about',
        ]
