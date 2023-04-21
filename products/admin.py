from django.contrib import admin
from .models import Animal,Category,SubCategory,Product,ProductImages,ProductVariant
# Register your models here.


admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(SubCategory)


class VariantInline(admin.TabularInline):
    model = ProductVariant
    
class ImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [
        VariantInline,
        ImagesInline
    ]


admin.site.register(Product,ProductAdmin)