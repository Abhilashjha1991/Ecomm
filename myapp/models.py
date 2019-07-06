from django.db import models
from django.db.models.signals import pre_save,post_save
from Ecommerce.utils import unique_slug_generator,get_unique_slug
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    seller=models.BooleanField("Seller status",default=False)
    buyer=models.BooleanField("Buyer status",default=False)


class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True,blank=True)

    class Meta:
        db_table="Categories"

    def __str__(self):
        return self.name
    '''
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self,'name','slug')
        super().save(*args,**kwargs)
    '''
class Product(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    seller=models.ForeignKey(User,on_delete=models.CASCADE,) #editable=false meanse nothing can edited,bydefault true
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True,blank=True)
    description=models.TextField(blank=True)
    pics=models.FileField(upload_to = 'pics',null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name

class image(models.Model):
    name = models.ForeignKey(Product,on_delete=models.CASCADE, default=None)
    pics = models.ImageField(upload_to = 'pics',null=True,verbose_name='Image')

State_CHOICES = (
    ('0','Select'),
    ('1','New Delhi'),
    ('2','Bihar'),
    ('3','Haryana'),
    ('4','Punjab'),
    ('6','Rajasthan'),
    ('7','Utterpradesh'),
    ('8','Maharashtra'),
    ('9','Kerala'),
    ('10','Jharkhand'),
)

class buyeraddress(models.Model):
    mobile=models.CharField(max_length=10)
    name=models.CharField(max_length=50) 
    HouseNo=models.CharField(max_length=50)
    Landmark=models.CharField(max_length=100)
    Locality=models.CharField(max_length=50)
    Area=models.CharField(max_length=50)
    #State=models.ForeignKey('States', on_delete=models.CASCADE ,null=True, blank=True)
    State=models.CharField(max_length=10, choices=State_CHOICES, default='Select')


    class Meta:
        db_table="buyeraddress"

    def __str__(self):
        return self.name

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance,'name','slug')
pre_save.connect(slug_generator,sender=Categories)
pre_save.connect(slug_generator,sender=Product)

