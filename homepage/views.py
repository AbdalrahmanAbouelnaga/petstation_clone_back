from django.shortcuts import render
from .serializers import BrandSerializer,CarouselItemSerializer
from rest_framework import viewsets,mixins
from .models import Brand,CarouselItem
# Create your views here.



class CarouselView(mixins.ListModelMixin,viewsets.GenericViewSet):
    serializer_class = CarouselItemSerializer

    def get_queryset(self):
        return CarouselItem.objects.filter(is_active=True)
    

class BrandView(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    lookup_field = "slug"