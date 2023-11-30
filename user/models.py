from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator

from .managers import UserManager
from utils.models import TimeStampModel
from common.models import Activity, District, CompanyType, Employee, Skill, DriverLicense

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    _validate_phone = RegexValidator(
        regex=r'^998[0-9]{9}$',
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan iborat bo'lishi kerak. Masalan: 998901235476"
    )
    phone_number = models.CharField(
        max_length=50, unique=True, validators=[_validate_phone]
    )
    email = models.EmailField(blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    @classmethod
    def is_phone_number_available(cls, phone_number):
        if cls.objects.filter(phone_number=phone_number).exists():
            return True
        return False


class CompanyProfile(TimeStampModel, User):
    title = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)

    about = models.TextField(blank=True, null=True)

    activity = models.ManyToManyField(Activity)

    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, blank=True, null=True)
    company_type = models.ForeignKey(
        CompanyType, on_delete=models.CASCADE, blank=True, null=True)

    logo = models.ImageField(upload_to='company/logo/', blank=True, null=True)
    main_image = models.ImageField(
        upload_to='company/main/', blank=True, null=True)

    active_time = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)


class GenderChoise(models.Choices):
    male = "Erkak"
    female = "Ayol"


class CurrencyChoice(models.Choices):
    Uzs = 'UZS'
    Usd = 'USD'


class JobSearcherProfile(User, TimeStampModel):
    # Relations
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True
    )
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, blank=True, null=True
    )
    skills = models.ManyToManyField(
        Skill, blank=True
    )
    driver_license = models.ManyToManyField(
        DriverLicense, blank=True
    )

    # Fields
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GenderChoise.choices)
    bithed_date = models.DateField()
    about = models.TextField()
    salary = models.IntegerField()
    currency = models.CharField(
        max_length=20, choices=CurrencyChoice.choices, default=CurrencyChoice.Uzs
    )
    is_freelancer = models.BooleanField(default=False)
