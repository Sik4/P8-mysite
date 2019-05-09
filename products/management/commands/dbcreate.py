from django.core.management.base import BaseCommand
import requests

from products.models import Product, Category


class Command(BaseCommand):
    help = 'Download products from Openfoodfacts'

    categories = ['Chocolates', 'Pizzas', 'Sauces', 'Fishes']

    def create_db(self):
        for category in self.categories:
            new_category = Category.objects.create(name=category)

            parameters = {
                'action': 'process',
                'json': 1,
                'page_size': 20,
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category

            }
            response = requests.get('https://world.openfoodfacts.org/cgi/search.pl', params=parameters)
            data = response.json()
            products = data['products']

            for product in products:
                try:
                    new_product = {
                        'new_category': new_category,
                        'product_name': product['product_name'],
                        'nutrition_grade_fr': product['nutrition_grade_fr'],
                        'code': product['code'],
                        'url': product['url'],
                        'image_url': product['image_url'],
                        'image_nutrition_url': product['image_nutrition_url'],
                    }
                    print(new_product)
                    Product.objects.get_or_create(**new_product)

                except KeyError as e:
                    print('Error is :', e)
                    pass

    def handle(self, *args, **options):
        self.create_db()



