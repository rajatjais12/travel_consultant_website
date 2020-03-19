from django.db import models
from django.urls import reverse
from package.models import Product
class Cntnt(models.Model):
    product = models.ForeignKey(Product, related_name='product_del',verbose_name=('product') ,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=300, db_index=True)
    desc1=models.CharField(max_length=150, db_index=True)
    desc1=models.CharField(max_length=150, db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'cntnt'
        verbose_name_plural = 'cntnts'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:list_by_cntnt', args=[self.name])
    def get_absolute_url_p(self):
        return reverse('blog:details',args=[self.product])
    def get_absolute_url_sub_product(self):
        return reverse('blog:sub_details',args=[self.slug])   

# Create your models here.
