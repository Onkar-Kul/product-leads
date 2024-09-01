from django.urls import path

from products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, TopTenProductsAPIView, \
    BottomTenProductsAPIView

urlpatterns = [
    path('create/', ProductListCreateAPIView.as_view(), name='product-creation'),
    path('list/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('update/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),
    path('retrieve/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),
    path('delete/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),

    # Reporting APIs (Products Related)
    path('top-ten-products/', TopTenProductsAPIView.as_view(), name='top-ten-products'),
    path('bottom-ten-products/', BottomTenProductsAPIView.as_view(), name='bottom-ten-products'),

]
