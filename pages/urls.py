from django.urls import path, include
from . import views
urlpatterns = [
    path('', view=views.HomePageView.as_view(), name='home'),
    path('about', view=views.AboutPageView.as_view(), name='about')
]
