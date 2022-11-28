from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_api),
    path('<int:id>', views.product_api),
    path('popular', views.popular),
    path('active', views.active),
    path('active/<int:id>', views.active),
    path('addFromProvider', views.add_product_from_provider),
    path('search', views.search_product),
    path('type', views.product_by_type)
]
