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

    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name