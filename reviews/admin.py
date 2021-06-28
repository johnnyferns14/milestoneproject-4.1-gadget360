from django.contrib import admin

from reviews.models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'gadget',
        'customer',
        'review_title',
        'review_description',
        'date_added',
    )


admin.site.register(ProductReview, ProductReviewAdmin)
