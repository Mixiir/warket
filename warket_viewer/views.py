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
    template_name = 'list_wines.html'
    context_object_name = 'wines_data'

    def get_queryset(self):
        wines = Wine.objects.all()

        search = self.request.GET.get('search')
        if search:
            wines = wines.filter(
                Q(name__icontains=search) |
                Q(variety__icontains=search) |
                Q(vintage__icontains=search) |
                Q(type__icontains=search) |
                Q(grape_variety__icontains=search))

        return wines

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context


class DetailWine(DetailView):
    model = Wine
    template_name = 'detail_wine.html'
    context_object_name = 'wine_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context


class CreateWine(PermissionRequiredMixin, CreateView):
    permission_required = 'warket_viewer.add_wine'
    model = Wine
    fields = '__all__'
    template_name = 'create_wine.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context
