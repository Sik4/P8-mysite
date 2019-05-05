from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Download products from Openfoodfacts'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Hello World'))

