from unittest import SimpleTestCase
from django.urls import reverse, resolve
from .stock_ms.stock_service.views import product_api, popular, active, add_product_from_provider, product_by_type, search_product


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, product_api)
    
    def test_popular_url_is_resolves(self):
        url = reverse('product_popular')
        self.assertEquals(resolve(url).func, popular)
    
    def test_active_url_is_resolves(self):
        url = reverse('product_active')
        self.assertEquals(resolve(url).func, active)
    
    def test_add_product_from_provider_url_is_resolves(self):
        url = reverse('add_from_provider')
        self.assertEquals(resolve(url).func, add_product_from_provider)
    
    def test_search_url_is_resolves(self):
        url = reverse('product_search')
        self.assertEquals(resolve(url).func, search_product)
    
    def test_product_by_type_url_is_resolves(self):
        url = reverse('product_by_type')
        self.assertEquals(resolve(url).func, product_by_type)
