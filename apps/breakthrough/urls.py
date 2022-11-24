from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("members", MembersView.as_view(), name="members"),
    path("", MembersView.as_view(), name="dashboard"),
    path("reports", MembersView.as_view(), name="reports"),
    path("profile", ProfileView.as_view(), name="profile"),
]