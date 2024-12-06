from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()

    image = models.ImageField(upload_to='menu/', default=f'menu/{name}.jpg')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart {self.id}'
    
    def total_carbs(self):
        total = 0
        for entry in self.cartentry_set.all():
            total += entry.carbohydrates()
        return total
    
    def total_protein(self):
        total = 0
        for entry in self.cartentry_set.all():
            total += entry.protein()
        return total
    
    def total_fat(self):
        total = 0
        for entry in self.cartentry_set.all():
            total += entry.fat()
        return total
    
    def total_calories(self):
        total = 0
        for entry in self.cartentry_set.all():
            total += entry.calories()
        return total
    
    def total(self):
        total = 0
        for entry in self.cartentry_set.all():
            total += entry.total()
        return total

class CartEntry(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity}x {self.item.name}'

    def total(self):
        return self.quantity * self.item.price
    
    def calories(self):
        return self.quantity * self.item.calories
    
    def protein(self):
        return self.quantity * self.item.protein
    
    def fat(self):
        return self.quantity * self.item.fat
    
    def carbohydrates(self):
        return self.quantity * self.item.carbohydrates
    
    def cost(self):
        return self.quantity * self.item.price