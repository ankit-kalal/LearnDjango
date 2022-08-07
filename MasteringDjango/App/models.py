from django.db import models
# from django.contrib.auth.models import User

from accounts.models import CustomUser as User
from django.core.validators import RegexValidator

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name  = models.CharField(max_length=255)
    primary_key  = models.FloatField()

    @classmethod
    def updatePrice(cls, product_id, price):
        product = cls.objects.filter(product_id  = product_id).first()
        product.price = price
        product.save()
        return product
        

    @classmethod
    def craeteProduct(cls, product_name,price):
        product = Product(product_name = product_name, price = price)
        product.save()
        return product

    # @staticmethod
    # def a_static_method():
    #     """A static method has no information about instances or classes
    #     unless explicitly given. It just lives in the class (and thus its 
    #     instances') namespace.
    #     """
    #     return "something"

    def __str__(self):
        return self.product_name



class CartManager(models.Manager):
    def create_cart(self,user):
        cart = self.create(user=user)
        #we can perform more actions here
        return cart

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField()

    objects = CartManager()
    


class ProductInCart(models.Model):
    class Meta:
        unique_together = ('cart','product')

    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()




class Order(models.Model):
    status_choices = (
        (1,"Not Packed"),
        (2,"Ready For Shipment"),
        (3,"Shipped"),
        (4,"Delivered")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choices,default=1)



class Deal(models.Model):
    user = models.ManyToManyField(User)
    deal_name = models.CharField(max_length=255)




class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=5)
    phone_regex = RegexValidator( regex = r'^\d{10}$',message = "phone number should exactly be in 10 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex])
    query = models.TextField()