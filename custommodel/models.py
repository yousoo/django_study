from django.db import models
from django.contrib.auth.models import AbstractUser

class Members(AbstractUser):
    member_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=100)
    introduce = models.TextField()

    def __str__(self):
        return f'{self.username}({self.member_name})'