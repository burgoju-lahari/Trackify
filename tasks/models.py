from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models. CASCADE)
    title = models.CharField(max_length = 200)    #title ->text field
    completed = models.BooleanField(default = False)   #completed -> true/false checkbox
    
    def __str__(self):   #__str__ -> how it shows in admin panel
        return self.title