from django.urls import path

from . import views

urlpatterns = [
    path('language/add/list/', views.LanguageCreateListView.as_view())
]
