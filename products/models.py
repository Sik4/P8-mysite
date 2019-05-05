from django.db import models

# Create your models here.


class Product(models.Model):
    """
    fields from :
    https://en.wiki.openfoodfacts.org/Fields_used
    """
    # Product name
    product_name = models.CharField(max_length=200)
    # nutriscore (a to e)
    nutrition_grade_fr = models.CharField(max_length=1)
    # unique code, PK
    code = models.BigIntegerField(primary_key=True)
    # url of the product (TextField over CharField = no limitation in max_length)
    url = models.TextField()
    # standard url image
    image_url = models.TextField()
    # url image etiquette (try image_thumb_url)
    image_small_url = models.TextField()

    def __str__(self):
        return self.product_name


