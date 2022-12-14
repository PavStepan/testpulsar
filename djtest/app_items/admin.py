from django.contrib import admin
from app_items.models import FormatModel, ItemModel, StatusModel


admin.site.register(FormatModel)
admin.site.register(ItemModel)
admin.site.register(StatusModel)
