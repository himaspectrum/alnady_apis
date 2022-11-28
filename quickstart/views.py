from pprint import pprint
from .models import Product,ProductDetails
from rest_framework import generics
from .serializers import ProductSerializer,DetailCosmeticsshortnameSerializer,ProductBatchesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ProductBatches(generics.CreateAPIView):  
    serializer_class = ProductBatchesSerializer


class ListProduct(generics.ListAPIView):  
    serializer_class = ProductSerializer

    def get_queryset(self): 
        # Product = next((m for m in apps.get_models() if m._meta.db_table=='PRODUCT'), None)
        response = Product.objects.all()
        return response 

class DetailCosmeticsshortnameView(generics.ListAPIView):
    serializer_class = DetailCosmeticsshortnameSerializer
    http_method_names = ['patch','get']

    def get_queryset(self, *args, **kwargs):
        product_obj = Product.objects.filter(notification_no=self.kwargs["pk"]).first()
        pprint(product_obj)
        qs = ProductDetails.objects.filter(product_id=product_obj.id)
        return qs
    
    def patch(self,request, *args, **kwargs):
        base_response = super(DetailCosmeticsshortnameView, self).patch(request, *args, **kwargs)
        return base_response
