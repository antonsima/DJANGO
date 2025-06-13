from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.add_product"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_published = True
        return super().form_valid(form)

    def has_permission(self):
        return self.request.user.is_authenticated


class ProductsListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    success_url = reverse_lazy("catalog:products_list")
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(is_published=True).order_by("name")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_info.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.can_change_product"

    def has_permission(self):
        obj = self.get_object()
        return obj.owner == self.request.user or super().has_permission()


class ProductUnpublishView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = []
    template_name = "catalog/product_confirm_unpublish.html"
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.can_unpublish_product"

    def form_valid(self, form):
        form.instance.is_published = False
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.can_delete_product"

    def has_permission(self):
        obj = self.get_object()
        return obj.owner == self.request.user or super().has_permission()


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
