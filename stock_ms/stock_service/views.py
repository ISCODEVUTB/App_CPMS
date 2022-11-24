from .models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import requests
from django.db.models import Q


@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        if id:
            product = Product.objects.filter(id=id)
            if product:
                product_serilizer = ProductSerializer(product, many=True)
                return JsonResponse(product_serilizer.data[0], safe=False)
            else:
                return JsonResponse({"response": "product not found"}, safe=False)
        else:
            products = Product.objects.all()
            product_serilizer = ProductSerializer(products, many=True)
            return JsonResponse(product_serilizer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serilizer = ProductSerializer(data=product_data)
        if product_serilizer.is_valid():
            product_serilizer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(id=product_data['id'])
        product_serilizer = ProductSerializer(product, data=product_data)
        if product_serilizer.is_valid():
            product_serilizer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully", safe=False)


def popular(request):
    if request.method == 'GET':
        product = Product.objects.filter(Price__lte=30000, Active=True)
        product_serilizer = ProductSerializer(product, many=True)
        return JsonResponse(product_serilizer.data, safe=False)


def active(request, id=0):
    if request.method == 'GET':
        if id:
            product = Product.objects.filter(id=id, Active=True)
            if product:
                product_serilizer = ProductSerializer(product, many=True)
                return JsonResponse(product_serilizer.data[0], safe=False)
            else:
                return JsonResponse({"response": "product not found"}, safe=False)
        else:
            product = Product.objects.filter(Active=True)
            product_serilizer = ProductSerializer(product, many=True)
            return JsonResponse(product_serilizer.data, safe=False)


@csrf_exempt
def addProductFromProvider(request):
    if request.method == 'GET':
        response1 = requests.get(
            'https://provider-serviceutb.onrender.com/providers')
        providers = response1.json()
        return JsonResponse(providers['data'], safe=False)

    elif request.method == 'POST':
        provider_name = request.GET['name']
        id_prod = request.GET['id_prod']
        requested_quantity = request.GET['quantity']

        response1 = requests.get(
            'https://provider-serviceutb.onrender.com/providers')
        providers = response1.json()

        for provider in providers['data']:
            if provider['name'] == provider_name:
                id_provider = provider['id']

        response2 = requests.get(
            'https://provider-serviceutb.onrender.com/provider/'+str(id_provider)+'/'+str(id_prod))
        product1 = response2.json()

        product1['Quantity'] = requested_quantity

        product_filter = Product.objects.filter(
            Q(Provider_id_prod=product1['Provider_id_prod']) & Q(Provider_id=product1['Provider_id']))

        if product_filter and requested_quantity:
            product2 = Product.objects.get(
                Provider_id_prod=product1['Provider_id_prod'], Provider_id=product1['Provider_id'])
            data = {'Quantity': product2.Quantity + int(requested_quantity)}
            product_serilizer = ProductSerializer(
                product2, data=data, partial=True)
            if product_serilizer.is_valid():
                product_serilizer.save()
                return JsonResponse({"Updated successfully": product_serilizer.data}, safe=False)
            return JsonResponse("Failed to Add", safe=False)
        else:
            if product_filter:
                return JsonResponse("Product already in stock and no quantity provided", safe=False)
            else:
                product_serilizer = ProductSerializer(data=product1)
                if product_serilizer.is_valid():
                    product_serilizer.save()
                    return JsonResponse("Added Succesfully", safe=False)
                return JsonResponse("Failed to Add", safe=False)


def SearchProduct(request):
    if request.method == 'GET':

        name = request.GET['name']

        product = Product.objects.filter(
            Q(Name__startswith=str.lower(name)) |
            Q(Name__contains=name) |
            Q(Name__startswith=str.upper(name)) |
            Q(Name__contains=str.upper(name[0])+name[1:]))
        product_serilizer = ProductSerializer(product, many=True)
        if product:
            return JsonResponse(product_serilizer.data, safe=False)
        else:
            return JsonResponse("No products found", safe=False)


def ProductByType(request):
    if request.method == 'GET':

        type_prod = request.GET['type']
        product = Product.objects.filter(Q(Type__startswith=str.lower(
            type_prod[0])) | Q(Type__startswith=str.upper(type_prod[0])))
        product_serilizer = ProductSerializer(product, many=True)

        if product:
            return JsonResponse(product_serilizer.data, safe=False)
        else:
            return JsonResponse("No products found", safe=False)
