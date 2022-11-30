from django.db import models
from django.contrib.auth import get_user_model

class Snack (models.Model):  
    name = models.CharField(max_length=64, help_text="chips", default="snack") 
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default = 'description')

    def __str__(self):
        return self.name