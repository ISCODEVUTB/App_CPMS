from django.urls import path
from . import views

urlpatterns = [
    path('', views.productApi),
    path('<int:id>', views.productApi),
    path('popular', views.popular),
    path('active', views.active),
    path('active/<int:id>', views.active),
    path('addFromProvider', views.addProductFromProvider),
    path('search', views.SearchProduct),
    path('type', views.ProductByType)
]
