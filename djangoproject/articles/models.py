from pyexpat import model
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from articles.utils import slugify_instance_title
from django.urls import reverse

# Create your models here.
class Articles(models.Model): # All the class in models must import from models.Model
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # auto_now : Whenever Model saved, time added
    # auto_now_add : Whenever model added, time added
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def get_absolute_url(self):
        # return f'/articles/{self.slug}/'
        return reverse("article-detail", kwargs={"slug":self.slug})

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Articles)

def article_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")
    if created:
        slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Articles)