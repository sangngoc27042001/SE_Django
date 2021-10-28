from django.db import models
from django.db.models.fields.related import ManyToManyField
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here.
country_arr=(('France','France'),('England','England'),('Japan','Japan'))
type_arr=(('Food','Food'),('Drink','Drink'))

class dish(models.Model):
    name=models.CharField(unique=True, primary_key=True, max_length=50)
    image=models.FileField(blank=True, null=True, upload_to='photos')
    country=models.CharField(blank=True, null=True, choices=country_arr,max_length=50)
    type=models.CharField(choices=type_arr,max_length=50)
    price=models.DecimalField(max_digits=5,decimal_places=2,blank=True, null=True)

class bill_item(models.Model):
    item_name=models.ForeignKey(dish, on_delete=models.SET_NULL, null=True, blank=True,related_name='bill')
    amount=models.PositiveSmallIntegerField()
        
class bill_order(models.Model):
    bill_item=models.ManyToManyField(bill_item, null=True, blank=True)
    cus_phone= PhoneNumberField(unique = False, null = False, blank = False) # Here
    date=models.DateField(null=True,auto_now_add=True)
    finish=models.BooleanField(auto_created=False)

    def total_price(self):
        sum=0
        for item in self.bill_item.all():
            sum+=item.amount*item.item_name.price
        return sum
    price_total=models.DecimalField(max_digits=7,decimal_places=2,blank=True, null=True)
    def save(self, *args,**kwargs):
        try:
            self.price_total=self.total_price()
        except:
            pass
        super().save(*args,**kwargs)
    

class restaurant(models.Model):
    name=models.CharField(unique=True, primary_key=True,max_length=50)
    address=models.TextField()
    dishes=models.ManyToManyField(dish, null=True, blank=True)



