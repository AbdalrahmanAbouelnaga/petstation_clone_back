from rest_framework import serializers
from . import models
from django.urls import reverse
from homepage.serializers import BrandSerializer
from django.db.models import Q

class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProductVariant
        fields = (
            "id",
            "size",
            "price",
        )

class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self,obj):
        return self.context.get('request').build_absolute_uri(obj.image.url)
    
    class Meta:
        model = models.ProductImages
        fields = (
            "image",
        )

class ProductListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    variants = VariantSerializer(many=True)
    images = serializers.SerializerMethodField()
    brand = BrandSerializer()
    
    def get_images(self,obj):
        data = models.ProductImages.objects.filter(product=obj)
        serializer = ImageSerializer(data,many=True,context={"request":self.context.get("request")})
        return serializer.data


    def get_url(self,obj):
        return reverse("product-detail",kwargs={"animal_slug":obj.sub_category.category.animal.slug,
                                                        "category_slug":obj.sub_category.category.slug,
                                                        "sub_category_slug":obj.sub_category.slug,
                                                        "slug":obj.slug})
    class Meta:
        model = models.Product
        fields = (
            "id",
            "url",
            "title",
            "size",
            "brand",
            "has_variants",
            "variants",
            "images",
            "price",
        )

class SubCategoryDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    products = ProductListSerializer(many=True)

    def get_url(self,obj):
        return reverse("sub_category-detail",kwargs={"animal_slug":obj.category.animal.slug,
                                                     "category_slug":obj.category.slug,
                                                     "slug":obj.slug})
    
    class Meta:
        model = models.SubCategory
        fields = (
            "url",
            "title",
            "products"
        )


class SubCategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def get_products(self,obj):
        prods = models.Product.objects.filter(sub_category__category__animal__slug=obj.category.animal.slug,sub_category__category=obj.category,sub_category=obj)
        data =  ProductListSerializer(prods,many=True,context={"request":self.context.get("request")}).data
        return data

    def get_url(self,obj):
        return reverse("sub_category-detail",kwargs={"animal_slug":obj.category.animal.slug,
                                                     "category_slug":obj.category.slug,
                                                     "slug":obj.slug})
    
    class Meta:
        model = models.SubCategory
        fields = (
            "url",
            "title",
            "products"
        )


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)
    url = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def get_products(self,obj):
        prods = models.Product.objects.filter(sub_category__category__animal__slug=obj.animal.slug,sub_category__category=obj)
        data =  ProductListSerializer(prods,many=True,context={"request":self.context.get("request")}).data
        return data

    def get_url(self,obj):
        return reverse("category-detail",kwargs={"animal_slug":obj.animal.slug,"slug":obj.slug})
    

    class Meta:
        model = models.Category
        fields = (
            "url",
            "title",
            "sub_categories",
            "products"
        )
        lookup_field = "slug"


class AnimalSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    def get_products(self,obj):
        sizes = self.context.get("request").query_params.get('sizes')
        brands = self.context.get("request").query_params.get('brands')
        prods = models.Product.objects.filter(sub_category__category__animal__slug=obj.slug)
        print(brands)
        if sizes is not None:
            prods = prods.filter(Q(size = sizes) | Q(variants__size=sizes))
        if brands is not None:
            prods = prods.filter(Q(brand__slug=brands))
        data =  ProductListSerializer(prods,many=True,context={"request":self.context.get("request")}).data
        return data

    def get_url(self,obj):
        return reverse("animal-detail",kwargs={"slug":obj.slug})
    class Meta:
        model = models.Animal
        fields = (
            "id",
            "url",
            "title",
            "products",
            "image"
        )



class NavSubCatSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        return reverse("sub_category-detail",kwargs={"animal_slug":obj.category.animal.slug,
                                                     "category_slug":obj.category.slug,
                                                     "slug":obj.slug})
    
    class Meta:
        model = models.SubCategory
        fields = (
            "url",
            "title",
        )


class NavCatSerializer(serializers.ModelSerializer):
    sub_categories = NavSubCatSerializer(many=True)
    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        return reverse("category-detail",kwargs={"animal_slug":obj.animal.slug,"slug":obj.slug})
    

    class Meta:
        model = models.Category
        fields = (
            "url",
            "title",
            "sub_categories"
        )
        lookup_field = "slug"


class NavAnimalSerializer(serializers.ModelSerializer):
    categories = NavCatSerializer(many=True)
    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        return reverse("animal-detail",kwargs={"slug":obj.slug})
    class Meta:
        model = models.Animal
        fields = (
            "id",
            "url",
            "title",
            "categories",
            "image"
        )