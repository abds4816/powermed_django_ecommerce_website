from django.contrib import admin
from .models import Order, OrderItem



class OrderItemAdmin(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
	list_filter = ('is_finished',)
	search_fields = ['first_name','last_name','city']
	inlines = [
	OrderItemAdmin,
	]

admin.site.register(Order, OrderAdmin)