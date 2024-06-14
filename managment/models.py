from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    role = models.CharField(max_length = 6)

    def __str__ (self):
        return self.name