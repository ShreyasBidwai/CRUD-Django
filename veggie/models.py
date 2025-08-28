from django.db import models

class Receipe(models.Model):
    name = models.CharField(max_length=100),
    desc = models.TextField(null=False),
    img = models.ImageField(upload_to="recipes")
