from django.contrib import admin

from shop.models import Product, Category, Comment, Order

# Register your models here.


admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Order)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    fields = ('title',)
    pass
    # prepopulated_fields = {'slug': ('title',)}
