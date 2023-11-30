from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, CompanyProfile, JobSearcherProfile
from .forms import UserCreationForm, CompanyProfileCreateForm, JobSearcherProfileCreateForm

from common.admin import LanguageInline, EducationInline, SocialMediaInline

# Register your models here.


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    add_form = UserCreationForm
    list_display = [
        "phone_number",
        'email',
        'is_admin',

    ]
    list_display_links = [
        "phone_number",
        'email',
        'is_admin',

    ]
    list_filter = []
    fieldsets = [
        (None, {"fields": [
            "phone_number",
            'email',
            'is_admin',
            'password',
        ]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "phone_number",
                    'email',
                    'is_admin',
                    # 'is_staff',
                    'password1',
                    'password2',
                ],
            },
        ),
    ]
    ordering = ["id"]


@admin.register(CompanyProfile)
class CompanyProfileAdmin(UserAdmin):
    list_display = [
        'phone_number',
        'title',
        'legal_name',
        'email',
        # 'logo',
    ]
    model = CompanyProfile
    add_form = CompanyProfileCreateForm
    list_display = [
        'title',
        'legal_name',
        'phone_number',
        'email',
    ]
    list_display_links = [
        'title',
    ]
    list_filter = []
    fieldsets = [
        (None, {
            "fields": [
                'phone_number',
                'email',
                'title',
                'legal_name',
                'activity',
                'district',
                'about',
                'employee',
                'company_type',
                'logo',
                'main_image',
                'active_time',
                'website',
                'password',
            ]
        }),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    'phone_number',
                    'email',
                    'title',
                    'legal_name',
                    'activity',
                    'district',
                    'about',
                    'employee',
                    'company_type',
                    'logo',
                    'main_image',
                    'active_time',
                    'website',
                    'password1',
                    'password2',
                ],
            },
        ),
    ]
    ordering = ["id"]


@admin.register(JobSearcherProfile)
class JobSearcherProfileAdmin(UserAdmin):
    list_display = [
        'full_name',
        'phone_number',
        'gender',
        'bithed_date',
        'is_freelancer',
    ]

    model = JobSearcherProfile
    add_form = JobSearcherProfileCreateForm

    inlines = [LanguageInline, SocialMediaInline, EducationInline]

    list_display_links = [
        'full_name',
    ]
    list_filter = []
    fieldsets = [
        (None, {
            "fields": [
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
                'password',
            ]
        }),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
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
                    'password1',
                    'password2',
                ],
            },
        ),
    ]
    ordering = ["id"]
