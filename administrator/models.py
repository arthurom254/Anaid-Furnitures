from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

TRUE_FALSE=(
    ("True","True"),
    ("False","False"),
)

class Category(models.Model):
    title=models.CharField(max_length=100, unique=True)
    description=models.TextField(max_length=100, blank=True, null=True)
    img=models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title

class ItemImg(models.Model):
    title=models.CharField(max_length=100)  
    img=models.ImageField(upload_to='uploads/prouct')
    img1=models.ImageField(upload_to='uploads/prouct', null=True, blank=True)
    img2=models.ImageField(upload_to='uploads/prouct', null=True, blank=True)
    img3=models.ImageField(upload_to='uploads/prouct', null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.id}" 
 
 
class Sizes(models.Model):
    width=models.DecimalField(max_digits=5, decimal_places=1)
    height=models.DecimalField(max_digits=5, decimal_places=1)
    def __str__(self):
        return f"{self.width} by {self.height}"


class Description(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.title}"

class Item(models.Model):           
    title = models.CharField(max_length=100, unique=True)
    description = models.ManyToManyField(Description)
    img=models.ForeignKey(ItemImg, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    price2=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    category=models.ManyToManyField(Category)
    trending=models.CharField(max_length=5, choices=TRUE_FALSE, null=True)
    available=models.IntegerField()
    offer=models.CharField(max_length=5, choices=TRUE_FALSE, default='False')
    outofstalk=models.CharField(max_length=5, choices=TRUE_FALSE,default="False")
    size=models.ManyToManyField(Sizes, blank=True)

    def get_absolute_url(self):
        first=self.category.first()
        return reverse('product_more',[str(first) ,self.id])

    def __str__(self):
        return self.title
       
class Review(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    stars=models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    title=models.CharField(max_length=100, null=True, blank=True)
    text=models.TextField(max_length=500 , null=True, blank=True)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user} Review on {self.item}"

class CartToken(models.Model):
    id=models.AutoField(primary_key=True)
    token=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.token}" 


class Cart(models.Model):
    token=models.ForeignKey(CartToken, on_delete=models.CASCADE , null=True)
    item=models.ForeignKey(Item, on_delete=models.CASCADE , null=True)
    qty=models.IntegerField(default=1)
    price=models.IntegerField(null=True)
    checked=models.CharField(max_length=10, choices=TRUE_FALSE, default='False')
    
    def __str__(self):
        return f"{self.token}"


class UserProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile=models.ImageField(upload_to='', default='profile.svg')
    phone=models.CharField(max_length=15, default='')
    
    def __str__(self):
        return f"{self.user}"
    
class Country(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        ordering=['name']

class City(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    class Meta:
        ordering=['name']

class Station(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    prce=models.IntegerField()
    def __str__(self):
        return f"{self.city} - {self.name}"
    class Meta:
        ordering=['name']
    
class DeliveryLocations(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    station=models.ForeignKey(Station, on_delete=models.CASCADE, null=True, blank=True)
    towndelivery=models.CharField(max_length=10, choices=TRUE_FALSE, default='False') 
    phone=models.CharField(max_length=15, default='')
    fname=models.CharField(max_length=100, default='')
    lname=models.CharField(max_length=100, default='')


    
    def __str__(self):
        return f"{self.user} -  {self.station}"
    # class Meta:
    #     ordering=['country','city','station']
        

class Order(models.Model):
    invoice=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    location=models.ForeignKey(DeliveryLocations,on_delete=models.CASCADE, null=True)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateTimeField(default=timezone.now)
    order_complete=models.CharField(max_length=10, choices=TRUE_FALSE, default='False')
    order_status=models.CharField(max_length=10, choices=TRUE_FALSE, default='False')
    payment_status=models.CharField(max_length=10, choices=TRUE_FALSE, default='False')
    pickup_status=models.CharField(max_length=10, choices=TRUE_FALSE, default='False')
    
    def __str__(self):
        return f"{self.user} - {self.item}"


class PaymentInProgress(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    invoice=models.CharField(max_length=100)
    gross_pay=models.DecimalField(max_digits=10, decimal_places=2)
    payment_status=models.CharField(max_length=10, choices=TRUE_FALSE, default='False')
    token=models.ForeignKey(CartToken, on_delete=models.CASCADE , null=True)
    
    def __str__(self):
        return f"{self.invoice} - {self.user}"


class ActivityLog(models.Model):
    model_name = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.model_name} - {self.action}"
    

class SiteSettings(models.Model):
    sites_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=256)
    linkedin=models.CharField(max_length=256)
    shopify=models.CharField(max_length=256)
    facebook=models.CharField(max_length=256)
    instagram=models.CharField(max_length=256)
    twitter=models.CharField(max_length=256)
    phone=models.CharField(max_length=20)
    map=models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.sites_name}'s Site Settings"



