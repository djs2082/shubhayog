from django.db import models
from customer.models import CustomerModel
from guaranteer.models import GuaranteerModel
import datetime
# Create your models here.


class LoanTypeModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="LOAN NAME", max_length=50,null=False,blank=False)

    class Meta:
        verbose_name = "LOAN TYPE"
        verbose_name_plural = "LOAN TYPES"

    def __str__(self):
        return str(self.name)

class LoanModel(models.Model):
    id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(CustomerModel, null=False,blank=False,verbose_name="CUSTOMER NAME", on_delete=models.PROTECT)
    guaranteer=models.ForeignKey(GuaranteerModel,null=True,verbose_name="GUARANTEER NAME", on_delete=models.PROTECT)
    loantype=models.ForeignKey(LoanTypeModel, verbose_name="LOAN TYPE", null=False,blank=False,on_delete=models.PROTECT)
    amount=models.IntegerField(verbose_name="LOAN AMOUNT",null=False,blank=False)
    installment=models.IntegerField(verbose_name="INSTALLMENT AMOUNT",null=False,blank=False)
    installment_date=models.DateField(verbose_name="INSTALLMENT DATE", null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)
    # raw_id_fields = ("guaranteer",)
    class Meta:
        verbose_name = "LOAN"
        verbose_name_plural = "LOANS"

    def __str__(self):
        return str(self.id)+" "+str(self.customer.fname)+" "+str(self.customer.lname)+" : "+str(self.amount)+" : "+str(self.installment_date)


class LoanRemaining(models.Model):
    id=models.AutoField(primary_key=True)
    loan=models.ForeignKey(LoanModel, verbose_name="TOTAL LOAN", on_delete=models.CASCADE)
    total_amount=models.IntegerField(verbose_name="TOTAL LOAN AMOUNT",null=False,blank=False)
    amount_paid=models.IntegerField(verbose_name="AMOUNT PAID",null=False,blank=False)
    amount_remaining=models.IntegerField(verbose_name="AMOUNT REMAINING",null=False,blank=False)
    date_time=models.DateTimeField(verbose_name="DATE AND TIME", default=datetime.datetime.now())
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "LOAN REMAINING"
        verbose_name_plural = "LOAN REMAININGS"

    def __str__(self):
        return str(self.loan.customer.fname)+" "+str(self.loan.customer.lname)+" : "+str(self.total_amount)+"-"+str(self.amount_paid)+"="+str(self.amount_remaining)
    

