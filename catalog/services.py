from .models import Product


class CategoryService:
    """Сервис для работы с продуктами категорий с кэшированием"""

    @classmethod
    def get_products_by_category(cls, category_id):
        return Product.objects.filter(
            category_id=category_id, is_published=True
        ).order_by("name")
