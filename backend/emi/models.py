from django.db import models
from loan.models import LoanModel
from datetime import date
# Create your models here.
class EMIModel(models.Model):
    id=models.AutoField(primary_key=True)
    loan=models.ForeignKey(LoanModel, null=False,blank=False,verbose_name="LOAN DETAILS", on_delete=models.CASCADE)
    amount=models.IntegerField(verbose_name="EMI AMOUNT",null=False,blank=False)
    deadline_date=models.DateField(verbose_name="LAST DATE FOR THIS EMI")
    date=models.DateField(verbose_name="DATE", default=date.today())
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "EMI"
        verbose_name_plural = "EMIS"

    def __str__(self):
        return str(self.loan.customer.fname)+" "+str(self.loan.customer.lname)+" : "+str(self.amount)+" : "+str(self.date)
