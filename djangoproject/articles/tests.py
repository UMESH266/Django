from django.test import TestCase
from django.utils.text import slugify
# Create your tests here.
from .models import Articles

class AritcleTestCase(TestCase):
    def test_hellow_world_unique_slug(self):
        qs = Articles.objects.exclude(slug__iexact='hello-world')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertEqual(slug, slugified_title)