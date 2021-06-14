from django.contrib import admin
from .models import gadgetAttr


class gadgetAttrAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'asins',
        'dimensions',
        'imageurls',
        'price'
    )

    ordering = ('asins', )


admin.site.register(gadgetAttr, gadgetAttrAdmin)
