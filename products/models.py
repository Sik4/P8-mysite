from django.db import models

# Create your models here.


class Products(models.Model):
    products_title = models.CharField(max_length=200)
    products_content = models.TextField()
    products_published = models.DateTimeField("date published")

    def __str__(self):
        return self.products_title
