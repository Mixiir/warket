import django.contrib.auth.decorators
import django.db.models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .constants import LANGUAGES, COUNTRIES
from .models import Wine, Manufacturer, Cart
from django.db.models import Q
from django.contrib import messages
from django.forms import HiddenInput
from .forms import CreateWineForm
from django.http import HttpResponse


# Create your views here.

def get_country_name(country_code):
    for country in COUNTRIES:
        if country[0] == country_code:
            return country[1]


def get_languages_name(language_code):
    for language in LANGUAGES:
        if language[0] == language_code:
            return language[1]


class WineSortedList(ListView):
    model = Wine
    template_name = 'list_wines.html'
    context_object_name = 'wines_data'

    def get_queryset(self):
        wines = Wine.objects.all()
        search = self.request.GET.get('show_only')
        if search:
            wines = wines.filter(Q(type__icontains=search))
        return wines


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
                Q(type__icontains=search)
            )
        return wines

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context


class ManufacturersListView(ListView):
    model = Manufacturer
    template_name = 'list_manufacturers.html'
    context_object_name = 'manufacturers_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'manufacturers'
        return context


class DetailManufacturer(DetailView):
    model = Manufacturer
    template_name = 'detail_manufacturer.html'
    context_object_name = 'manufacturer_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'manufacturer'
        return context


class CreateManufacturer(PermissionRequiredMixin, CreateView):
    template_name = 'create_manufacturer.html'
    model = Manufacturer
    success_url = reverse_lazy('list_manufacturers')
    fields = '__all__'
    permission_required = 'viewer.add_manufacturer'


class UpdateManufacturer(PermissionRequiredMixin, UpdateView):
    template_name = 'update_manufacturer.html'
    model = Manufacturer
    success_url = reverse_lazy('list_manufacturers')
    fields = '__all__'
    permission_required = 'viewer.change_manufacturer'


class DeleteManufacturer(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_manufacturer.html'
    model = Manufacturer
    success_url = reverse_lazy('list_manufacturers')
    context_object_name = 'manufacturer'
    permission_required = 'viewer.delete_manufacturer'


class DetailWine(DetailView):
    model = Wine
    template_name = 'detail_wine.html'
    context_object_name = 'wine_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context


def create_wine(request):
    if request.method == 'POST':
        form = CreateWineForm(request.POST, request.FILES)
        if form.is_valid():
            create_wine_form = form.save(commit=False)
            create_wine_form.user = request.user
            create_wine_form.save()
            messages.success(request, f'Wine has been listed')
            return redirect('list_wines')
    else:
        form = CreateWineForm()
    return render(request, 'create_wine.html', {'form': form})


class EditWine(PermissionRequiredMixin, UpdateView):
    permission_required = 'warket_viewer.edit_wine'
    model = Wine
    fields = '__all__'
    widgets = {'user': HiddenInput()}
    template_name = 'edit_wine.html'
    success_url = reverse_lazy('list_wines')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'wines'
        return context


class CartListView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart_data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_is'] = 'cart'
        wine_full_price = 0
        for wine in Cart.objects.filter(user=self.request.user):
            wine_single_price = wine.wine.price_per_unit * wine.quantity
            wine_full_price += wine_single_price
        context['total'] = wine_full_price
        return context


class AddToCart(PermissionRequiredMixin, CreateView):
    permission_required = 'warket_viewer.add_cart'
    model = Cart
    fields = '__all__'
    template_name = 'add_to_cart.html'
    context_object_name = 'cart_data'
    success_url = reverse_lazy('list_wines')


class RemoveFromCart(PermissionRequiredMixin, DeleteView):
    permission_required = 'warket_viewer.delete_cart'
    model = Cart
    success_url = reverse_lazy('list_wines')
    context_object_name = 'cart_data'
    template_name = 'remove_from_cart.html'
