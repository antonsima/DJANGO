from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"
        ordering = [
            "name",
        ]


User = get_user_model()


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="catalog/images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберите категорию продукта",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        null=True,
        blank=True,
        related_name="products",
    )

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
        ]
        permissions = [
            ("can_unpublish_product", "Может снимать с публикации продукты"),
            ("can_delete_product", "Может удалять любые продукты"),
            ("can_change_product", "Может изменять любые продукты"),
        ]
