from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Tag)
admin.site.register(models.Customer)
admin.site.register(models.Order)

