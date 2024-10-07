from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Car, Color, Brand


class CarApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            list_cars = []
            cars = Car.objects.all()
            for car in cars:
                list_cars.append({
                    "id": car.id,
                    "name": car.name,
                    "description": car.description,
                    "color": car.color.pk,
                    "price": car.price,
                    "brand": car.brand.pk,
                    "year": car.year
                })

            return Response({"Cars" : list_cars})
        try:
            car = Car.objects.get(pk=pk)
            return Response(model_to_dict(car))
        except:
            return Response({"Error": "Car not found"}, status=404)

class ColorApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            list_colors = []
            colors = Color.objects.all()
            for color in colors:
                list_colors.append({
                    "id": color.id,
                    "name": color.name
                })

            return Response({"Colors" : list_colors})
        try:
            color = Color.objects.get(pk=pk)
            return Response(model_to_dict(color))
        except:
            return Response({"Error": "Color not found"})

class BrandApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            list_brands = []
            brands = Brand.objects.all()
            for brand in brands:
                list_brands.append({
                    "id": brand.id,
                    "name": brand.name
                })

            return Response({"Brands" : list_brands})
        try:
            brand = Brand.objects.get(pk=pk)
            return Response(model_to_dict(brand))
        except:
            return Response({"Error": "Brand not found"})





