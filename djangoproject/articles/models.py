from pyexpat import model
from django.db import models

# Create your models here.
class Articles(models.Model): # All the class in models must import from models.Model
    title = models.TextField()
    content = models.TextField()