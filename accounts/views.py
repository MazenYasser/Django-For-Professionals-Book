from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
