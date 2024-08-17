from django.contrib import admin
from .models import NetworkLink


class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'title_product', 'model_product', 'release_date', 'debt', 'created_at', 'level']
    search_fields = ['name', 'country', 'city']
    list_filter = ['city']
    actions = ['clear_debt']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(NetworkLink, NetworkLinkAdmin)

