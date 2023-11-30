from django.contrib import admin

from .models import Language, SocialMedia, Education, LanguageDegree, LanguageType, District, DriverLicense, Skill, MediaType, Employee, CompanyType, Country, Activity, Experience


class LanguageInline(admin.StackedInline):
    model = Language
    extra = 1


class SocialMediaInline(admin.StackedInline):
    model = SocialMedia
    extra = 1


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1


admin.site.register(Language)
admin.site.register(SocialMedia)
admin.site.register(Education)
admin.site.register(LanguageDegree)
admin.site.register(LanguageType)
admin.site.register(District)
admin.site.register(DriverLicense)
admin.site.register(Skill)
admin.site.register(MediaType)
admin.site.register(Employee)
admin.site.register(CompanyType)
admin.site.register(Country)
admin.site.register(Activity)
admin.site.register(Experience)
