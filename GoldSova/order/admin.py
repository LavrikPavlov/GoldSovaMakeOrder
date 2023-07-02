from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

from .models import MakeOrder

class MakeOrderResorce(resources.ModelResource):
    class Meta:
        model = MakeOrder
        fields = ['number_oreder','order','file_order','status_order','created', 'uploaded']
        import_id_fields = ['number_oreder']

@admin.register(MakeOrder)
class MakeOrderAdmin(ImportExportActionModelAdmin):
    resource_class = MakeOrderResorce
    list_display = ['number_order','email','file_order','status_order','created', 'uploaded']
    list_editable = ['status_order']
    list_filter = ['status_order', 'created', 'uploaded']
