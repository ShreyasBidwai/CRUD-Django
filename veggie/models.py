from django.db import models

class Recipe(models.Model):
    img = models.ImageField(upload_to="recipes", null=True)
    desc = models.TextField(default='none')
    namer = models.CharField(max_length=100)

    def __str__(self):
        return self.namer
