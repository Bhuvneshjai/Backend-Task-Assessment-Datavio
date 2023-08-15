from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(null=True,blank=True)
    review_count = models.PositiveIntegerField()
    ratings = models.DecimalField(max_digits=3,decimal_places=2)
    media_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title