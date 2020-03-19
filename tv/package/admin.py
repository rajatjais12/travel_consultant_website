from django.contrib import admin
from .models import Category, Product,Price_list,fest_offer,Theme


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','image']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','created_at', 'updated_at','image']
    list_filter = ['created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
class offerAdmin(admin.ModelAdmin):
	list_display = ['name', 'offer','image']
admin.site.register(fest_offer, offerAdmin)		  

class themAdmin(admin.ModelAdmin):
	list_display = ['name','image']
admin.site.register(Theme, themAdmin)#admin.site.register(price_list)	
class PriceAdmin(admin.ModelAdmin):
	list_display = ['name','price_range']
admin.site.register(Price_list, PriceAdmin)
# Register your models here.


# Register your models here.


