from django.contrib import admin
from .models import Category,Brand,Color,Size,Product,ProductAttribute

admin.site.register(Size)

class BrandAdmin(admin.ModelAdmin):
    list_display=('id','title','image_tag')
    readonly_fields=('image_tag',)
admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','title','image_tag')
    readonly_fields=('image_tag',)
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display=('id','title','color_code','color_bg')
    readonly_fields=('color_bg',)
admin.site.register(Color,ColorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','image_tag','title','category','brand','status')
    list_editable=('status',)
    readonly_fields=('image_tag',)
admin.site.register(Product,ProductAdmin)

# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('id','product','price','color_bg','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)
