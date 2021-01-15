from django.urls import path

from . import views


urlpatterns = [
    path("", views.CompanyView.as_view()),
    path("<int:pk>/", views.CompanyDetailView.as_view(), name="company"),
]