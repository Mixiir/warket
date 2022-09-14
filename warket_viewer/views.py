import io
import os
import uuid

import decouple
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import Q
from django.forms import HiddenInput
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)
from PIL import Image

from cart.forms import CartAddProductForm

from .constants import COUNTRIES
from .forms import CreateWineForm, FormAPI
from .models import Manufacturer, Wine


def get_country_name(country_code):
    for country in COUNTRIES:
        if country[0] == country_code:
            return country[1]


class WineSortedList(ListView):
    model = Wine
    template_name = "list_wines.html"
    context_object_name = "wines_data"

    def get_queryset(self, **kwargs):
        wines = Wine.objects.all()
        if self.request.GET.get("show_only"):
            search = self.request.GET.get("show_only")
        else:
            search = ""
        context = super().get_context_data(**kwargs)
        context["page_is"] = wines
        if search:
            wines = wines.filter(Q(type__icontains=search))
        return wines, context


class WineListView(ListView):
    model = Wine
    template_name = "list_wines.html"
    context_object_name = "wines_data"

    def get_queryset(self):
        wines = Wine.objects.exclude(units_in_stock=0)
        #        wines = Wine.objects.all_auction_listings()
        search = self.request.GET.get("search")
        if search:
            wines = wines.filter(
                Q(name__icontains=search) |
                Q(vintage__icontains=search) |
                Q(type__icontains=search)
            )
        return wines

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_is"] = "wines"
        return context


class ManufacturersListView(ListView):
    model = Manufacturer
    template_name = "list_manufacturers.html"
    context_object_name = "manufacturers_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_is"] = "manufacturers"
        return context


class DetailManufacturer(DetailView):
    model = Manufacturer
    template_name = "detail_manufacturer.html"
    context_object_name = "manufacturer_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_is"] = "manufacturer"
        return context


class CreateManufacturer(CreateView):
    template_name = "create_manufacturer.html"
    model = Manufacturer
    success_url = reverse_lazy("list_manufacturers")
    fields = "__all__"


class UpdateManufacturer(UpdateView):
    template_name = "update_manufacturer.html"
    model = Manufacturer
    success_url = reverse_lazy("list_manufacturers")
    fields = "__all__"


class DeleteManufacturer(DeleteView):
    template_name = "delete_manufacturer.html"
    model = Manufacturer
    success_url = reverse_lazy("list_manufacturers")
    context_object_name = "manufacturer"


class DeleteWine(DeleteView):
    template_name = "delete_wine.html"
    model = Wine
    success_url = reverse_lazy("list_wines")
    context_object_name = "wine"


class DetailWine(DetailView):
    model = Wine
    template_name = "detail_wine.html"
    context_object_name = "wine_data"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context["page_is"] = "wines"
        context["cart_product_form"] = cart_product_form
        return context


class EditWine(UpdateView):
    model = Wine
    fields = "__all__"
    widgets = {"user": HiddenInput()}
    template_name = "edit_wine.html"
    success_url = reverse_lazy("list_wines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["manufacturer"] = Manufacturer.objects.all()
        context["page_is"] = "wines"
        return context


@login_required
def edit_wine(request, pk):
    wine = Wine.objects.get(pk=pk)
    form = CreateWineForm(request.POST or None, instance=wine)
    manufacturer = Manufacturer.objects.all()
    if form.is_valid():
        form.save()
        return redirect("list_wines")
    return render(
        request,
        "edit_wine.html",
        {"form": form, "manufacturer": manufacturer, "wine": wine},
    )


@login_required
def create_wine(request):
    mode = "rapidapi"
    rapidapi_key = decouple.config("RAPIDAPI_KEY")
    options = {
        "rapidapi": {
            "url": "https://wine-recognition2.p.rapidapi.com/v1/results",
            "headers": {"X-RapidAPI-Key": rapidapi_key}
        }
    }
    main_form = CreateWineForm(request.POST or None, request.FILES or None)
    search_form = FormAPI(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if search_form.is_valid() and not request.POST.get("price_per_unit"):
            if request.FILES:
                image = request.FILES["image"]
            else:
                image = "default.jpg"
            response = requests.post(
                options[mode]["url"],
                headers=options[mode]["headers"],
                files={"image": (os.path.basename(image.name), image)})
            if response.status_code == 200:
                try:
                    data = response.json().get("results")
                    if len(data) > 0:
                        results = data[0]
                        info = results.get("entities")[0].get("classes")
                        name = list(info.keys())[0]
                        if name[-4:].isnumeric():
                            year = int(name[-4:])
                            first_dict_name = (name[:-5]).title()
                        else:
                            year = "."
                            first_dict_name = name
                        messages.success(
                            request,
                            "Wine image has been identified"
                        )
                        main_form = CreateWineForm(
                            initial={
                                "name": first_dict_name,
                                "vintage": year
                            }
                        )
                        return render(
                            request,
                            "create_wine.html",
                            {
                                "year": year,
                                "first_dict_name": first_dict_name,
                                "main_form": main_form,
                            }
                        )
                    else:
                        messages.error(request, "data[0] not > 0")
                except Exception as e:
                    messages.error(request, f"Error: {e}.")
        elif main_form.is_valid():
            create_wine_form = main_form.save(commit=False)
            if request.FILES:
                thumbnail = request.FILES["image"]
                thumbnail = Image.open(thumbnail)
                thumbnail.thumbnail((200, 320), Image.ANTIALIAS)
                thumbnail_io = io.BytesIO()
                unique_filename = uuid.uuid4().hex
                thumbnail.save(thumbnail_io, format="JPEG")
                thumbnail_file = InMemoryUploadedFile(
                    thumbnail_io,
                    None,
                    unique_filename + ".jpg",
                    "image/jpeg",
                    thumbnail_io.getbuffer().nbytes,
                    None
                )
            else:
                thumbnail_file = "default.jpg"
            create_wine_form.thumbnail = thumbnail_file
            create_wine_form.user = request.user
            create_wine_form.save()
            messages.success(request, "Wine has been listed")
            return redirect("list_wines")
        else:
            messages.error(
                request,
                "Error: Wine has not been listed, because form is not valid"
            )
    else:
        main_form = CreateWineForm()
        manufacturer = Manufacturer.objects.all()
    return render(
        request,
        "create_wine.html",
        {
            "main_form": main_form,
            "manufacturer": manufacturer
        }
    )


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_is"] = "home"
        return context


class Base(TemplateView):
    template_name = "base.html"
