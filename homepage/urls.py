from  django.urls import path
from . import views

urlpatterns = [
    path("carousel/",views.CarouselView.as_view({"get":"list"})),
    path("brands/",views.BrandView.as_view({"get":"list"}),name="brand-list"),
    path("brands/<slug:slug>/",views.BrandView.as_view({"get":"retrieve"}),name="brand-detail")
]