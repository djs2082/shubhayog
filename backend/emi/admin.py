from django.contrib import admin
from emi.models import EMIModel
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Register your models here.
admin.site.register(EMIModel)

class EMIAdmin(admin.ModelAdmin):
    search_fields=('amount')
