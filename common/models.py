from django.db import models
from utils.models import TimeStampModel


# Create your models here.


class Activity(TimeStampModel):
    title = models.CharField(max_length=255)
    sub_activity = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True
    )


class Country(TimeStampModel):
    title = models.CharField(max_length=255)


class District(TimeStampModel):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class CompanyType(TimeStampModel):
    title = models.CharField(max_length=255)


class Employee(TimeStampModel):
    title = models.CharField(max_length=255)


class MediaType(TimeStampModel):
    logo = models.ImageField(
        upload_to='media_type/logo/', blank=True, null=True)
    title = models.CharField(max_length=255)


class SocialMedia(TimeStampModel):
    url = models.URLField()
    user = models.ForeignKey('user.JobSearcherProfile',
                             on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)


class EduLevelChoise(models.Choices):
    MediumSpecial = "O'rta Maxsus"
    Bachelor = "Bakalavr"
    Master = "Magistr"


class Education(TimeStampModel):
    user = models.ForeignKey('user.JobSearcherProfile',
                             on_delete=models.CASCADE, related_name='educations')
    title = models.CharField(max_length=255)
    level = models.CharField(max_length=50, choices=EduLevelChoise.choices)
    direction = models.CharField(max_length=255)
    begin_month = models.CharField(max_length=50)
    begin_year = models.CharField(max_length=50)
    finish_month = models.CharField(max_length=50, blank=True, null=True)
    finish_year = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField()


class Experience(TimeStampModel):
    user = models.ForeignKey('user.JobSearcherProfile',
                             on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    begin_month = models.CharField(max_length=50)
    begin_year = models.CharField(max_length=50)
    finish_month = models.CharField(max_length=50, blank=True, null=True)
    finish_year = models.CharField(max_length=50, blank=True, null=True)
    about = models.TextField()


class LanguageType(TimeStampModel):
    title = models.CharField(max_length=255)


class LanguageDegree(TimeStampModel):
    title = models.CharField(max_length=255)


class Language(TimeStampModel):
    user = models.ForeignKey('user.JobSearcherProfile',
                             on_delete=models.CASCADE, related_name='languages')
    language = models.ForeignKey(LanguageType, on_delete=models.CASCADE)
    degree = models.ForeignKey(LanguageDegree, on_delete=models.CASCADE)


class Skill(TimeStampModel):
    title = models.CharField(max_length=255)


class DriverLicense(TimeStampModel):
    title = models.CharField(max_length=255)
