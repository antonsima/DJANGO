from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from django.views.generic.edit import CreateView

from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    success_url = reverse_lazy("catalog:products_list")
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_info.html"
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if name and phone and message:
            return HttpResponse(
                f'Спасибо, {name}! Ваш контактный номер {phone} и сообщение "{message}" успешно отправлены.'
            )
        return HttpResponse("Заполните имя, телефон и сообщение!", status=400)
