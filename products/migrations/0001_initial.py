# Generated by Django 2.2 on 2019-05-09 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_name', models.CharField(max_length=200)),
                ('nutrition_grade_fr', models.CharField(max_length=1)),
                ('code', models.BigIntegerField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('image_url', models.TextField()),
                ('image_nutrition_url', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Category')),
            ],
        ),
    ]
