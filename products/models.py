from django.db import models
from slugify import slugify
from homepage.models import Brand
# Create your models here.


class Animal(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to="upload/",blank=True,null=True)

    def __str__(self):
        return self.title
    def save(self):
        self.slug = slugify(self.title)
        return super().save()


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    animal = models.ForeignKey(Animal,related_name="categories",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def save(self):
        self.slug = slugify(self.title)
        return super().save()
    

class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)
    category = models.ForeignKey(Category,related_name="sub_categories",on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def save(self):
        self.slug = slugify(self.title)
        return super().save()


class Product(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(editable=False)
    has_variants = models.BooleanField(default=False)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    sub_category = models.ForeignKey(SubCategory,related_name="products",on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products")

    def save(self):
        self.slug = slugify(self.title)
        return super().save()

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/")


class ProductVariant(models.Model):
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    product = models.ForeignKey(Product,related_name="variants",on_delete=models.CASCADE)
