# Generated by Django 3.0.8 on 2020-07-20 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='labels',
            field=models.CharField(blank=True, choices=[('New Arrivals', 'New Arrivals'), ('Best Sellers', 'Best Sellers'), ('Features', 'Features')], max_length=50, null=True),
        ),
    ]
