from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Articles(models.Model): # All the class in models must import from models.Model
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # auto_now : Whenever Model saved, time added
    # auto_now_add : Whenever model added, time added
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")
    if instance.slug is None:
        instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender=Articles)

def article_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

post_save.connect(article_post_save, sender=Articles)