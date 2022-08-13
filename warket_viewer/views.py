from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .constants import LANGUAGES, COUNTRIES
from .models import Wine, Profile, Cart
from django.db.models import Q


# Create your views here.

def get_country_name(country_code):
    for country in COUNTRIES:
        if country[0] == country_code:
            return country[1]


def get_languages_name(language_code):
    for language in LANGUAGES:
        if language[0] == language_code:
            return language[1]


class WineListView(ListView):
    model = Wine
    template_name = 'wines_list.html'
    context_object_name = 'wines_data'

    def get_queryset(self):
        wines = Wine.objects.all()

        search = self.request.GET.get('search')
        if search:
            wines = wines.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(rating__name__icontains=search) |
                Q(price__bio__icontains=search) |
                Q(country__name__icontains=search) |
                Q(region__bio__icontains=search) |
                Q(grape_variety__icontains=search) |
                Q(vintage__icontains=search) |
                Q(color__icontains=search) |
                Q(alcohol_content=search))
        return wines

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context


class RegisterUser(CreateView):
    model = Profile
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'register'
        return context
