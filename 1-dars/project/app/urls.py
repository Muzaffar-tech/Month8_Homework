from django.urls import path
from .views import CarApiView, ColorApiView, BrandApiView

urlpatterns = [
    path('cars/', CarApiView.as_view()),
    path('cars/<int:pk>', CarApiView.as_view()),
    path('colors/', ColorApiView.as_view()),
    path('colors/<int:pk>', ColorApiView.as_view()),
    path('brands/', BrandApiView.as_view()),
    path('brands/<int:pk>', BrandApiView.as_view())
]
