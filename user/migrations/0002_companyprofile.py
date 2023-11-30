# Generated by Django 4.2.7 on 2023-11-27 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('legal_name', models.CharField(max_length=255)),
                ('about', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/logo/')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='company/main/')),
                ('active_time', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('activity', models.ManyToManyField(to='common.activity')),
                ('company_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.companytype')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.district')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.employee')),
            ],
            options={
                'abstract': False,
            },
            bases=('user.user', models.Model),
        ),
    ]
