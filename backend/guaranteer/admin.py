from django.contrib import admin
from guaranteer.models import GuaranteerModel

# Register your models here.
admin.site.register(GuaranteerModel)

class GuranteerAdmin(admin.ModelAdmin):
    raw_id_fields = ("fname",)
