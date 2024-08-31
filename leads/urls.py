from django.urls import path

from leads.views import LeadCreateView

urlpatterns = [
    path('create/', LeadCreateView.as_view(), name='lead-creation'),
    # path('list/', ProductListCreateAPIView.as_view(), name='product-list'),
    # path('update/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),
    # path('retrieve/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),
    # path('delete/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-update'),


]
