from .models import Brand,CarouselItem
from rest_framework import serializers
from django.urls import reverse


class BrandSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        return reverse("brand-detail",kwargs={"slug":obj.slug})

    class Meta:
        model = Brand
        fields = (
            "title",
            "image",
            "url",
            "slug"
        )


class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = (
            "title",
            "image",
            "url",
            "priority"
        )