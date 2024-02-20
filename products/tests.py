from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from products.serializers import PhoneSerializer, TvSerializer
from products.views import ProductAPIViewBase, ProductDetailAPIView
from .models import Tv, Laptop, Phone, Earbud

class ProductAPIViewTests(TestCase):
    #setup the instances of models used in the test
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='test_user', email='test@mail.com')
        self.tv = Tv.objects.create(model='Test TV', brand='Test brand', screen_size=55, price=999)
        self.phone = Phone.objects.create(model='Test TV', brand='Test brand', color='black', price=999)
        # self.laptop = Laptop.objects.create(model='Test Laptop', description='Test Description', price=1499)
        # self.earbud = Earbud.objects.create(model='Test Earbud', description='Test Description', price=199)
    
    # test get_serializer_class for tv
    def test_get_serializer_class_tv(self):
        view = ProductAPIViewBase()
        view.kwargs = {'product': 'tv'}
        self.assertEqual(view.get_serializer_class(), TvSerializer)
    
    # test get_serializer_class for tv
    def test_get_serializer_class_phone(self):
        view = ProductAPIViewBase()
        view.kwargs = {'product': 'phone'}
        self.assertEqual(view.get_serializer_class(), PhoneSerializer)

    def test_get_queryset_phone(self):
        view = ProductAPIViewBase()
        view.kwargs = {'product': 'phone'}
        self.assertQuerysetEqual(view.get_queryset(), Phone.objects.all())