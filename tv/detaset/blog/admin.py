from django.contrib import admin
from .models import Cntnt
# Register your models here.
class CntntAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','image']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Cntnt, CntntAdmin)
