from django.db.models import Count
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from leads.models import Lead
from leads.serializers import LeadSerializer, LeadProductCount
from products.views import CustomAPIViewMixin


# Create your views here.


class LeadCreateView(CustomAPIViewMixin, generics.CreateAPIView):
    """
            API view to handle creating Lead.
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
            Handle POST request to create Lead
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.create_response(data=serializer.data, message="Lead created successfully",
                                    status_code=status.HTTP_201_CREATED)


class LeadsBetweenDatesAPIView(CustomAPIViewMixin, APIView):
    """
        API view to retrieve leads created between specified start and end dates.

        This view requires authentication and accepts 'start_date' and 'end_date'
        as query parameters in the format 'YYYY-MM-DD'. It returns a list of leads
        created within the specified date range.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and retrieves
        leads within the specified date range.
        """
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        print(start_date, end_date)
        leads = Lead.objects.filter(created_at__range=[start_date, end_date])
        serializer = LeadSerializer(leads, many=True)
        return self.create_response(data=serializer.data, message="Leads retrieved successfully")


class LeadProductCountView(CustomAPIViewMixin, APIView):
    """
    API view to retrieve the Number of Products Inquired by Each Lead.

    This view annotates each lead with a count of the products they are
    interested in and returns information.
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and retrieves
        leads with their product counts.
        """
        leads = Lead.objects.annotate(product_count=Count('interested_products'))
        serializer = LeadProductCount(leads, many=True)
        return self.create_response(data=serializer.data, message="Lead product count retrieved successfully")