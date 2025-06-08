from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    context = {'products': products}

    return render(request, "catalog/home.html", context)


def contacts(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if name and phone and message:
            return HttpResponse(
                f'Спасибо, {name}! Ваш контактный номер {phone} и сообщение "{message}" успешно отправлены.'
            )
        return HttpResponse("Заполните имя, телефон и сообщение!", status=400)

    return render(request, "catalog/contacts.html")


def product_info(request: HttpRequest, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_info.html', {'product': product})