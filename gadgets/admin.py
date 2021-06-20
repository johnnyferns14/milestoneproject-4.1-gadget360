from django.contrib import admin
from .models import gadgetAttr, gadgetCategory


class gadgetAttrAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'brand',
        'asins',
        'dimensions',
        'imageurls',
        'price'
    )

    ordering = ('asins', )


admin.site.register(gadgetAttr, gadgetAttrAdmin)
admin.site.register(gadgetCategory)
