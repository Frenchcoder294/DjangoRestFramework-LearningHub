# import ptvsd
# ptvsd.enable_attach(address=("0.0.0.0", 5678))

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Tv, Phone, Laptop, Earbud
from .serializers import (
    TvSerializer,
    PhoneSerializer,
    EarbudSerializer,
    LaptopSerializer,
)

from django.core.cache import cache


class ProductAPIViewBase(generics.GenericAPIView):
    # authentication and permission classes are in settings.py

    def get_serializer_class(self):
        product = self.kwargs.get("product").capitalize()
        serializer_mapping = {
            "Tv": TvSerializer,
            "Phone": PhoneSerializer,
            "Laptop": LaptopSerializer,
            "Earbud": EarbudSerializer,
        }

        return serializer_mapping.get(product, None)

    def get_queryset(self):
        # check if queryset is cached
        queryset_cache_key = f"product_queryset_{self.kwargs.get('product')}"
        queryset = cache.get(queryset_cache_key)
        if queryset is None:
            product = self.kwargs.get("product").capitalize()
            model_mapping = {
                "Tv": Tv,
                "Phone": Phone,
                "Laptop": Laptop,
                "Earbud": Earbud,
            }
            model = model_mapping.get(product, None)
            queryset = model.objects.all() if model else None
            # Cache the queryset for future requests
            cache.set(queryset_cache_key, queryset)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get("pk")
        return get_object_or_404(queryset, pk=pk) if queryset else None


class ProductDetailAPIView(ProductAPIViewBase, generics.RetrieveAPIView):
    pass


class ProductListAPIView(ProductAPIViewBase, generics.ListAPIView):

    pass


class ProductCreateAPIView(ProductAPIViewBase, generics.CreateAPIView):

    def get(self, request, *args, **kwargs):
        print(self.request)
        return Response(
            {
                "message": f"using GET method only for creating a new {self.kwargs.get('product')}"
            },
            status=status.HTTP_200_OK,
        )

    def perform_create(self, serializer):
        serializer.save()


class ProductUpdateAPIView(ProductAPIViewBase, generics.UpdateAPIView):

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer_class = self.get_serializer_class()

        if obj and serializer_class:
            serializer = serializer_class(obj, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return super().update(request, *args, **kwargs)

        return self.http_method_not_allowed(request)

    # added for using patch, instead of put
    # def partial_update(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


class ProductDeleteAPIView(ProductAPIViewBase, generics.DestroyAPIView):

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({"message": f"Object {instance}successfully deleted"})
        else:
            return Response({"error": "Object not found"})
