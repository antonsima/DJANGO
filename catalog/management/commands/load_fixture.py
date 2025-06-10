import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Очищает базу данных и загружает в нее данные из фикстуры"

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        try:
            BASE_DIR = settings.BASE_DIR
            fixture_path = os.path.join(BASE_DIR, "catalog.json")

            call_command("loaddata", fixture_path, verbosity=2)

            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded fixture: {fixture_path}")
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading fixture: {e}"))
