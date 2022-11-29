from .models import Product
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_protect
import requests
from django.db.models import Q
from django.views.decorators.http import require_safe, require_GET, require_POST

failed_to_add = "Failed to Add"


# product API that contains all the CRUD actions.
@require_safe
@csrf_protect
def product_api(request, id=0):
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
        return JsonResponse(failed_to_add, safe=False)
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


# Return a Json of the products in the stock that have a price <= 30000.
@require_GET
@csrf_protect
def popular(request):
    if request.method == 'GET':
        product = Product.objects.filter(Price__lte=30000, Active=True)
        product_serilizer = ProductSerializer(product, many=True)
        return JsonResponse(product_serilizer.data, safe=False)


# Return a Json of the products that have the Active prop equal to True.
@require_GET
@csrf_protect
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

# Get all the providers from the providers service


@require_GET
@csrf_protect
def get_providers(request):
    if request.method == 'GET':
        # Request all the providers from the provider service.
        response1 = requests.get(
            'https://provider-serviceutb.onrender.com/providers')
        providers = response1.json()
        return JsonResponse(providers['data'], safe=False)


# Get the provider id from the provider service.
def get_provider_id(name):
    response1 = requests.get(
        'https://provider-serviceutb.onrender.com/providers')
    providers = response1.json()

    for provider in providers['data']:
        if provider['name'] == name:
            id_provider = provider['id']

    return str(id_provider)


# Get the parameters from the views to add a product from the provider
@csrf_protect
def get_params_for_provider_add(request):

    provider_name = request.GET['name']
    id_prod = request.GET['id_prod']
    requested_quantity = request.GET['quantity']

    return [provider_name, id_prod, requested_quantity]


# Add a product from the provider service.
@require_POST
@csrf_protect
def add_product_from_provider(request):
    # Request a specific product from a specific provider from the provider
    # service passing the id of the provider and the id of the product.
    response2 = requests.get(
        'https://provider-serviceutb.onrender.com/provider/'+get_provider_id(get_params_for_provider_add(request)[0])+'/'+str(get_params_for_provider_add(request)[1]))
    product1 = response2.json()

    product1['Quantity'] = get_params_for_provider_add(request)[2]

    product_filter = Product.objects.filter(
        Q(Provider_id_prod=product1['Provider_id_prod']) & Q(Provider_id=product1['Provider_id']))

    if product_filter and get_params_for_provider_add(request)[2]:
        product2 = Product.objects.get(
            Provider_id_prod=product1['Provider_id_prod'], Provider_id=product1['Provider_id'])
        data = {'Quantity': product2.Quantity +
                int(get_params_for_provider_add(request)[2])}
        product_serilizer = ProductSerializer(
            product2, data=data, partial=True)
        if product_serilizer.is_valid():
            product_serilizer.save()
            return JsonResponse({"Updated successfully": product_serilizer.data}, safe=False)
        return JsonResponse(failed_to_add, safe=False)
    else:
        if product_filter:
            return JsonResponse("Product already in stock and no quantity provided", safe=False)
        else:
            product_serilizer = ProductSerializer(data=product1)
            if product_serilizer.is_valid():
                product_serilizer.save()
                return JsonResponse("Added Succesfully", safe=False)
            return JsonResponse(failed_to_add, safe=False)


# Return a Json of the serached product if nothing is found return that.
@require_GET
@csrf_protect
def search_product(request):
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


# Return a Json the products depending on the type they have.
@require_GET
@csrf_protect
def product_by_type(request):
    if request.method == 'GET':

        type_prod = request.GET['type']
        product = Product.objects.filter(Q(Type__startswith=str.lower(
            type_prod[0])) | Q(Type__startswith=str.upper(type_prod[0])))
        product_serilizer = ProductSerializer(product, many=True)

        if product:
            return JsonResponse(product_serilizer.data, safe=False)
        else:
            return JsonResponse("No products found", safe=False)
