from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.
class Articles(models.Model): # All the class in models must import from models.Model
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # auto_now : Whenever Model saved, time added
    # auto_now_add : Whenever model added, time added
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)