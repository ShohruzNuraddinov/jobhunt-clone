from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('login/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('company/register/', views.CompanyRegisterView.as_view(),
         name='company_register'),
    path('company/register/verify/', views.CompanyRegisterVerify.as_view()),
    path('jobsearcher/register/', views.JobSearcherRegisterView.as_view()),
    path('jobsearcher/register/verify/', views.JobSearcherVerifyView.as_view()),

]
