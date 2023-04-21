from django.db import models
from rest_framework.exceptions import ValidationError
from slugify import slugify

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/")
    slug = models.SlugField(blank=True,null=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        return super().save()
    def __str__(self):
        return self.title


class CarouselItem(models.Model):
    image = models.ImageField(upload_to="upload/")
    title = models.CharField(max_length=200)
    url = models.URLField()
    PRIORITIES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
  )

    priority = models.IntegerField(default=0, choices=PRIORITIES)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
    
    def save(self):
        if self.is_active == True:
            all_active = type(self).objects.filter(is_active=True)
            if len(all_active) >= 7:
                raise ValidationError("Only a maximum of 7 carousel items can be active at the same time")
            if len(all_active.filter(priority=self.priority))>0:
                raise ValidationError("no two or more items can have the same priority.")
        return super().save()