# import ptvsd
# ptvsd.enable_attach(address=('0.0.0.0', 5678))

from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

from .models import Tv, Phone, Laptop, Earbud
from .serializers import TvSerializer, PhoneSerializer, EarbudSerializer, LaptopSerializer

class ProductAPIViewBase(generics.GenericAPIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        product = self.kwargs.get('product').capitalize()
        serializer_mapping = {
            'Tv': TvSerializer,
            'Phone': PhoneSerializer,
            'Laptop': LaptopSerializer,
            'Earbud': EarbudSerializer,
        }
        
        return serializer_mapping.get(product, None)

    def get_queryset(self):
        product = self.kwargs.get('product').capitalize()
        model_mapping = {
            'Tv': Tv,
            'Phone': Phone,
            'Laptop': Laptop,
            'Earbud': Earbud,
        }
        model = model_mapping.get(product, None)
        return model.objects.all() if model else None

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk) if queryset else None

class ProductDetailAPIView(ProductAPIViewBase, generics.RetrieveAPIView):
    pass

class ProductCreateAPIView(ProductAPIViewBase, generics.CreateAPIView):
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):   
        return Response({'message': 'GET method for creating a new product'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        
        serializer.save()

class ProductListAPIView(ProductAPIViewBase, generics.ListAPIView):
    #permission_classes = [permissions.DjangoModelPermissions]
    pass

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

class ProductDeleteAPIView(ProductAPIViewBase, generics.DestroyAPIView):

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({'message': f"Object {instance}successfully deleted"})
        else:
            return Response({'error': 'Object not found'})
