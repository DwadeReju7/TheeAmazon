from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
            # ... other fields

    def __str__(self):
        return self.name

class Categories(models.Model):
    category_name = models.CharField(max_length=50)
            # ... other fields

    def __str__(self):
        return self.category_name
    
class Products(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
            # ... other fields

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
            # ... other fields

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
    
class Order_Items(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
            # ... other fields

    def __str__(self):
      return  f"{self.quantity} x {self.product.product_name} (Order #{self.order.id})"
