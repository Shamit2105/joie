from django.db import models
from django.conf import settings

class Item(models.Model):
    seller=models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to = {'role':'seller'},
        related_name='items'
    )
    title = models.CharField(max_length=20)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField()

    def __str__(self):
        return self.name

    

