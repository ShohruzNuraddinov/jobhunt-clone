from django import forms
from django.core.exceptions import ValidationError

from .models import User, CompanyProfile, JobSearcherProfile


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            'phone_number',
            'email',
            # 'full_name',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CompanyProfileCreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = CompanyProfile
        fields = [
            'phone_number',
            'email',
            'title',
            'legal_name',
            'activity',
            'about',
            'employee',
            'company_type',
            'logo',
            'main_image',
            'active_time',
            'website',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        company = super().save(commit=False)
        company.set_password(self.cleaned_data["password1"])
        if commit:
            company.save()
        return company


class JobSearcherProfileCreateForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = JobSearcherProfile
        fields = [
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
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        jobsearcher = super().save(commit=False)
        jobsearcher.set_password(self.cleaned_data["password1"])
        if commit:
            jobsearcher.save()
        return jobsearcher
