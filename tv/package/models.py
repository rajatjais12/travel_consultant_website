from django.db import models
from django.urls import reverse

class fest_offer(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    offer = models.DecimalField(max_digits=10,decimal_places=0)
    class Meta:
        ordering = ('name', )
        index_together = (('id',),)

    def __str__(self):
        return self.name
    def get_absolute_url_offer(self):
        return reverse('package:offer_product_list', args=[self.slug])
class Price_list(models.Model):
    price_range=models.CharField(max_length=100,db_index=True)
    name=models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    class Meta:
        ordering = ('name', )
        index_together = (('name', 'slug'),)
    def __str__(self):
        return self.name    
    def get_absolute_url_price(self):
        return reverse('package:price_product_list', args=[self.slug])
class Theme(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
# Create your models here.
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
    def get_absolute_url_them(self):
        return reverse('package:theme_product_list', args=[self.slug])
LOCATION_CHOICES = (
    ('International Destinations','INTERNATIONAL'),
    ('Destinations within India', 'INDIA'),
)
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image_slid = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=300, db_index=True)
    Destinations = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='INTERNATIONAL')


    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('package:product_list_by_category', args=[self.slug])  

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    them_p = models.ForeignKey(Theme, related_name='them_products', on_delete=models.CASCADE)
    price_r= models.ForeignKey(Price_list, related_name='them_productf', on_delete=models.CASCADE)
    fest_f= models.ForeignKey(fest_offer, related_name='offer_products', on_delete=models.CASCADE)
    Destinations = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='INTERNATIONAL')

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('package:sub_product_list', args=[self.id, self.slug])  
    def get_absolute_url_price(self):
        return reverse('package:sub_product_list_price', args=[self.price])  
