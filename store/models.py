from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify




class Product(models.Model):

    LABELS = (
        ('New Arrivals', 'New Arrivals'),
        ('Best Sellers', 'Best Sellers'),
        ('Features', 'Features')
    )

    name             = models.CharField(max_length=50)
    image1           = models.ImageField(upload_to='Products/')
    image2           = models.ImageField(upload_to='Products/', null=True)
    description      = models.TextField(max_length=500)
    date_created     = models.DateTimeField(auto_now_add=False)
    slug             = models.SlugField(blank=True, null=True)
    price            = models.DecimalField(max_digits=5, decimal_places=2)
    labels           = models.CharField(max_length=50, choices=LABELS, null=True, blank=True)     
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def save(self , *args , **kwargs):
        if not self.slug :
            self.slug = slugify(self.name)
        super(Product , self).save(*args , **kwargs)

    def __str__(self):
        return self.name

    

