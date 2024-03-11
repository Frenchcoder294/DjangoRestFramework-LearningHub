from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from rest_framework import status


from products.serializers import (
    EarbudSerializer,
    LaptopSerializer,
    PhoneSerializer,
    TvSerializer,
)

from products.views import (
    ProductAPIViewBase,
    ProductCreateAPIView,
    ProductDetailAPIView,
)
from .models import Tv, Laptop, Phone, Earbud

# initiate user for auth tests
# user = User.objects.create_user(username="test_user", password="pass")


# test functions of view classes
class ProductAPIViewTests(TestCase):
    # setup the instances of models used in the test
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user", password="pass")
        self.tv = Tv.objects.create(
            model="Test TV", brand="Test brand", screen_size=55, price=999
        )
        # self.phone = Phone.objects.create(
        #     model="Test phone", brand="Test brand", color="black", price=999
        # )
        self.laptop = Laptop.objects.create(
            model="Test laptop", brand="Test brand", screen_size=15, price=999
        )
        self.earbud = Earbud.objects.create(
            model="Test earbud", brand="Test brand", with_lcd=False, price=999
        )

    # test get_serializer_class for tv
    def test_get_serializer_class_tv(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "tv"}
        self.assertEqual(view.get_serializer_class(), TvSerializer)

    # test get_serializer_class for laptop
    def test_get_serializer_class_laptop(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "laptop"}
        self.assertEqual(view.get_serializer_class(), LaptopSerializer)

    # test get_serializer_class for phone
    def test_get_serializer_class_phone(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "phone"}
        self.assertEqual(view.get_serializer_class(), PhoneSerializer)

    # test get_serializer_class for earbud
    def test_get_serializer_class_earbud(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "earbud"}
        self.assertEqual(view.get_serializer_class(), EarbudSerializer)

    def test_get_queryset_phone(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "phone"}
        self.assertQuerysetEqual(view.get_queryset(), Phone.objects.all())

    def test_get_obj_tv(self):
        view = ProductAPIViewBase()
        view.kwargs = {"product": "tv", "pk": "1"}
        self.assertEqual(view.get_object(), Tv.objects.get(pk=1))


# test urls (CRUD)
class APIUrlTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user", password="pass")
        self.tv = Tv.objects.create(
            model="Test TV", brand="Test brand", screen_size=55, price=999
        )

    def test_create_url(self):
        data = {
            "model": "Test phone",
            "brand": "Test brand",
            "color": "black",
            "price": 999,
        }

        self.client.login(username="test_user", password="pass")
        response = self.client.post("/products/phone/create/", data=data)

        # check response for creation of the instance
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Phone.objects.filter(model="Test phone").exists())

    def test_retrieve_url(self):
        # allow the test to follow the url to the redirected path
        response = self.client.get("/products/tv/1", follow=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["model"], "Test TV")
        self.assertEqual(response.json()["brand"], "Test brand")

    def test_update_url(self):
        data = {
            "model": "Test TV",
            "brand": "Test brand",
            "screen_size": 50,
            "price": 1100,
        }
        response = self.client.put("/products/tv/1/update/", data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["screen_size"], 50)
        self.assertEqual(response.json()["price"], "1100.00")


# test class for authentication
class ProductAuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user", password="pass")

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
        # User.objects.create_user(username="test_user", password="pass")
        self.client.login(username="test_user", password="pass")
        response = self.client.get("/products/tv/create/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_keyword(self):
        keyword = "Bearer"
        self.client.login()
        auth_endpoint = "http://localhost:8000/api/auth/"
        auth_response = self.client.post(
            auth_endpoint, {"username": "test_user", "password": "pass"}
        )
        self.assertEqual(auth_response.status_code, status.HTTP_200_OK)
        token = auth_response.json()['token']
        endpoint = "http://localhost:8000/products/phone/"
        response = self.client.get(
            endpoint, headers = {'Authorization': f'{keyword} {token}'}
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)