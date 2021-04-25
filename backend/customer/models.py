from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class CustomerModel(models.Model):
    mobile_regex = RegexValidator(regex=r"^\d{10}$")
    id = models.AutoField(primary_key = True)
    fname = models.CharField(verbose_name="FIRST NAME",max_length = 50)
    lname = models.CharField(verbose_name="LAST NAME",max_length = 50)
    mobile = models.CharField(verbose_name="MOBILE", validators=[mobile_regex],max_length=10,blank=False)
    email = models.EmailField(verbose_name="EMAIL", max_length = 254)
    address = models.CharField(verbose_name="ADDRESS",max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "CUSTOMER"
        verbose_name_plural = "CUSTOMERS"

    def __str__(self):
        return str(self.mobile)+":"+str(self.fname)+" "+str(self.lname)

