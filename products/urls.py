from django.urls import path
from . import views

urlpatterns = [
    path('<str:product>/', views.ProductListAPIView.as_view(), name='product-list'),
    path('<str:product>/<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<str:product>/create/', views.ProductCreateAPIView.as_view(), name='create-product'),
    path('<str:product>/<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='update_product,'),
    path('<str:product>/<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='delete_product'),
]