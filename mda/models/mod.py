from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=10, db_index=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.product_name
