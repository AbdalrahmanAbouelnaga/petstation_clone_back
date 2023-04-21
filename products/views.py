from django.shortcuts import render
from . import serializers,models
from rest_framework import viewsets,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


class AnimalView(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = serializers.AnimalSerializer
    lookup_field = "slug"
    queryset = models.Animal.objects.all()
     

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request":self.request})
        return context
        
class CategoryView(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request":self.request})
        return context
    
    def get_queryset(self):
        if self.action == "list":
            print(self.kwargs.get("animal_slug"))
            return models.Category.objects.filter(animal__slug=self.kwargs.get("animal_slug"))
        
    def get_object(self):
        return models.Category.objects.get(animal__slug=self.kwargs.get("animal_slug"),slug=self.kwargs.get("slug"))
    
class SubCategoryView(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):   

    lookup_field = "slug" 


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request":self.request})
        return context
    

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SubCategorySerializer
        if self.action == "retrieve":
            return serializers.SubCategoryDetailSerializer

    def get_queryset(self):
        if self.action == "list":
            return models.SubCategory.objects.filter(category__animal__slug=self.kwargs.get("animal_slug"),category__slug=self.kwargs.get("category_slug"))
    def get_object(self):
        return models.SubCategory.objects.get(category__animal__slug=self.kwargs.get("animal_slug"),category__slug=self.kwargs.get("category_slug"),slug=self.kwargs.get("slug"))
        


@api_view(["GET"])
def get_product(request,slug,animal_slug,category_slug,sub_category_slug):
    data = models.Product.objects.get(slug=slug,sub_category__slug=sub_category_slug,sub_category__category__slug=category_slug,sub_category__category__animal__slug=animal_slug)
    serializer = serializers.ProductListSerializer(data,context={"request":request})
    return Response(serializer.data,200)

class NavbarView(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = serializers.NavAnimalSerializer
    queryset = models.Animal.objects.all()

