from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductSerializer, TopAndBottomProductSerializer


# Create your views here.


class CustomAPIViewMixin:
    def create_response(self, data=None, message="Operation successful", status_code=status.HTTP_200_OK):
        response_data = {
            'message': message,
            'data': data
        }
        return Response(response_data, status=status_code)


class ProductListCreateAPIView(CustomAPIViewMixin, generics.ListCreateAPIView):
    """
        API view to handle listing and creating Product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """
                Handle GET requests to list all Products.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return self.create_response(data=serializer.data, message="Products retrieved successfully")

    def create(self, request, *args, **kwargs):
        """
            Handle POST request to create product
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.create_response(data=serializer.data, message="Product created successfully",
                                    status_code=status.HTTP_201_CREATED)


class ProductRetrieveUpdateDestroyAPIView(CustomAPIViewMixin, generics.RetrieveUpdateDestroyAPIView):
    """
        API view for retrieving, updating, or deleting a Product.
        This view handles GET, PUT/PATCH, and DELETE requests for individual Product.
        Permission required to access this view.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        """
            Retrieve a specific Product instance.

            Args:
                request (Request): The request object contains request data.

            Returns:
                Response: A Response object contains the product data and a success message.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.create_response(data=serializer.data, message="Product retrieved successfully")

    def update(self, request, *args, **kwargs):
        """
            Update a specific Product instance.

            Args:
                request (Request): The request object contains updated product.

            Returns:
                Response: A DRF Response object contains the serialized updated product data and a success message.
        """

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self.create_response(data=serializer.data, message="Product updated successfully")

    def destroy(self, request, *args, **kwargs):
        """
           Delete a specific Product.

           Args:
               request (Request): The request object.

           Returns:
               Response: A DRF Response object with a success message and an HTTP 204 status code.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return self.create_response(message="Product deleted successfully", status_code=status.HTTP_204_NO_CONTENT)


class TopTenProductsAPIView(CustomAPIViewMixin, APIView):
    """
       API view to retrieve the top 10 products with the highest lead.

       This view annotates products with the count of leads,
       filters products with at least one lead, and orders them by lead count
       in descending order, returning the top 10 products.
    """
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and retrieves
        the top 10 products based on lead count.
        """
        products = Product.objects.annotate(
            lead_count=Count('lead_interested_products')
        ).filter(lead_count__gte=1).order_by('-lead_count')[:10]
        serializer = TopAndBottomProductSerializer(products, many=True)
        return self.create_response(data=serializer.data, message="Top ten products retrieved successfully")


class BottomTenProductsAPIView(CustomAPIViewMixin, APIView):
    """
        API view to retrieve the bottom 10 products with the lowest lead.

        This view annotates products with the count of leads,
        orders them by lead count in ascending order, and returns the bottom 10 products.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
         Handles GET requests and retrieves the bottom 10 products based on lead.
        """
        products = Product.objects.annotate(lead_count=Count('lead_interested_products')).order_by('lead_count')[:10]
        serializer = TopAndBottomProductSerializer(products, many=True)
        return self.create_response(data=serializer.data, message="Bottom ten products retrieved successfully")

