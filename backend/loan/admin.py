from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from loan.models import LoanTypeModel,LoanModel,LoanRemaining
from emi.models import EMIModel
from loan.serializer import LoanRemainingSerializer
# Register your models here.
admin.site.register(LoanTypeModel)
admin.site.register(LoanModel)
admin.site.register(LoanRemaining)

# class LoanAdmin(admin.ModelAdmin):
#     raw_id_fields = ("guaranteer",)

@receiver(post_save,sender=EMIModel)
def update_remaining_amount(sender,instance,created,**kwargs):
    if created:
        data={}
        print(instance.loan.installment_date)
        data['loan']=instance.loan.id
        data['total_amount']=LoanRemaining.objects.latest('created_at').amount_remaining
        data['amount_paid']=instance.amount
        data['amount_remaining']=data['total_amount']-instance.amount
        print(data)
        serialized=LoanRemainingSerializer(data=data)
        if(serialized.is_valid(raise_exception = True)):
                saved = serialized.save()
        # print(loan_amount)
        print("HELLOW WORLD AFTER LONG TIME")


