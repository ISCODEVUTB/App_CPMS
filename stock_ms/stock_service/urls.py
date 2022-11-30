from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_api, name="home"),
    path('<int:id>', views.product_api, name="product_individual"),
    path('popular', views.popular, name="product_popular"),
    path('active', views.active, name="product_active"),
    path('active/<int:id>', views.active, name="product_active_by_id"),
    path('addFromProvider', views.add_product_from_provider, name="add_from_provider"),
    path('search', views.search_product, name="product_search"),
    path('type', views.product_by_type, name="product_by_type")
]
