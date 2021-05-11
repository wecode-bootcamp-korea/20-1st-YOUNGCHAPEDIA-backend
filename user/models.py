from django.db import models

# Create your models here.

class User(models.Model):
    name     = models.CharField(max_length=250)
    email    = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"