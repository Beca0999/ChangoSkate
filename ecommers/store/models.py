from django.db import models
import datetime

#Categoria de los productos
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    #@daverobb2011 
    class Meta:
        verbose_name_plural = 'Categories'
#Clientes
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


#Todos nuestros productos
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(max_length=500, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')
    # Agregar vendedor al modelo de producto
    is_saler = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2) 
    
    def __str__(self):
        return self.name


#Ordenes de compra del cliente
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) 
    address = models.CharField(max_length=250, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)  
    order_date = models.DateTimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product