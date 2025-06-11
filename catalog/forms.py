from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    BANNED_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование продукта"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )

        self.fields["image"].widget.attrs.update({"class": "form-control"})

        self.fields["category"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "").lower()
        description = cleaned_data.get("description", "").lower()

        for word in self.BANNED_WORDS:
            if word in name:
                self.add_error('name', f'Название продукта содержит запрещенное слово: {word}')
            if word in description:
                self.add_error('description', f'Описание продукта содержит запрещенное слово: {word}')

        return cleaned_data
