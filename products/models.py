from django.db import models

# Create your models here.


class Category(models.Model):
    # exposing the default model manager explicitly to override Pycharm
    objects = models.Manager()

    name = models.CharField(max_length=100)


class Product(models.Model):
    """
    fields from :
    https://en.wiki.openfoodfacts.org/Fields_used
    """
    # exposing the default model manager explicitly to override Pycharm
    objects = models.Manager()

    # Product name
    product_name = models.CharField(max_length=200)
    # Category
    new_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    # nutriscore (a to e)
    nutrition_grade_fr = models.CharField(max_length=1)
    # unique code, PK
    code = models.BigIntegerField(primary_key=True)
    # url of the product (TextField over CharField = no limitation in max_length)
    url = models.TextField()
    # standard url image
    image_url = models.TextField()
    # url image etiquette (try image_thumb_url)
    image_nutrition_url = models.TextField()

    def __str__(self):
        return self.product_name


