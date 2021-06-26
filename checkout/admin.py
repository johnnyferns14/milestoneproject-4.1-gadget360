from django.contrib import admin
from checkout.models import OrderDetail, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('total_lineitem')


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline)
    readonly_fields = ('order_number', 'order_date',
                       'delivery_cost', 'order_total',
                       'grand_total')

    fields = ('order_number', 'order_date', 'cust_name',
              'email_id', 'contact_number', 'country', 'postcode',
              'town_or_city', 'address1', 'address2', 'county',
              'delivery_cost', 'order_total', 'grand_total')

    list_display = ('order_number', 'order_date', 'cust_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date')


admin.site.register(OrderAdmin, OrderDetail)
