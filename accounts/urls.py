from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', view=views.SignupPageView.as_view(), name='signup'),
]
