from django.contrib import admin
from .models import Product

from guardian.admin import GuardedModelAdmin

@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    # list_display = ('names',)
    
    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        else:
            return True

    def has_view_permission(self, request, obj=None):
        pass











