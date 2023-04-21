from django.urls import path
from . import views

urlpatterns = [
    path("navbar/",views.NavbarView.as_view({"get":"list"})),
    path("",views.AnimalView.as_view({"get":"list"}),name="animal-list"),
    path("<slug:slug>/",views.AnimalView.as_view({"get":"retrieve"}),name="animal-detail"),
    path("<slug:animal_slug>/",views.CategoryView.as_view({"get":"list"}),name="category-list"),
    path("<slug:animal_slug>/<slug:slug>/",views.CategoryView.as_view({"get":"retrieve"}),name="category-detail"),
    path("<slug:animal_slug>/<slug:category_slug>/<slug:slug>/",views.SubCategoryView.as_view({"get":"retrieve"}),name="sub_category-detail"),
    path("<slug:animal_slug>/<slug:category_slug>/<slug:sub_category_slug>/<slug:slug>/",views.get_product,name="product-detail"),
]