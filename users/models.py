from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    q_choices = (
        ('What is the name of your favourite teacher?', 'teacher'),
        ('What is your favourite animal?', 'animal'),
        ('What is your favourite league team?', 'league'),
        ('Who is your favourite author?', 'author'),
        ('What is your comfort food?', 'comfort_food'),
    )
    security_question = models.CharField(max_length=255, choices=q_choices)
    security_answer = models.CharField(max_length=255, help_text="Answer to your security question")
    phone_number = models.CharField(max_length=10)

    @property
    def is_seller(self):
        return self.role == 'seller'
