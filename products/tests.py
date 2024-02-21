from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status


from products.serializers import LaptopSerializer, PhoneSerializer, TvSerializer


from products.views import ProductAPIViewBase, ProductDetailAPIView
from .models import Tv, Laptop, Phone, Earbud


class ProductAPIViewTests(TestCase):
    # setup the instances of models used in the test
    def setUp(self):
        self.client = APIClient()
        # self.user = User.objects.create(username='test_user', password='pass')
        self.tv = Tv.objects.create(
            model="Test TV", brand="Test brand", screen_size=55, price=999
        )
        self.phone = Phone.objects.create(
            model="Test TV", brand="Test brand", color="black", price=999
        )
        # self.laptop = Laptop.objects.create(model='Test Laptop', description='Test Description', price=1499)
        # self.earbud = Earbud.objects.create(model='Test Earbud', description='Test Description', price=199)

    # testing unauthenticated users
    def test_unauth_users(self):
        response = self.client.post(
            "/products/tv/create/",
            data={
                "brand": "samsung",
                "model": "d254",
                "price": 1959.97,
                "screen_sze": 55,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # testing authenticated user
    def test_auth_users(self):
        User.objects.create_user(username="test_user", password="pass")
        self.client.login(username="test_user", password="pass")
        response = self.client.get("/products/tv/create/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test get_serializer_class for tv
    def test_get_serializer_class_tv(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "tv"}
        self.assertEqual(view.get_serializer_class(), TvSerializer)

    def test_get_serializer_class_laptop(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "laptop"}
        self.assertEqual(view.get_serializer_class(), LaptopSerializer)

    # test get_serializer_class for phone
    def test_get_serializer_class_phone(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "phone"}
        self.assertEqual(view.get_serializer_class(), PhoneSerializer)

    def test_get_queryset_phone(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "phone"}
        self.assertQuerysetEqual(view.get_queryset(), Phone.objects.all())

    def test_get_obj_tv(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "tv", "pk": "1"}
        self.assertEqual(view.get_object(), Tv.objects.get(pk=1))
