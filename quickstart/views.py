from pprint import pprint
from .models import Product,Tempdrugsmanufacture
from rest_framework import generics
from .serializers import ProductSerializer
from django.apps import apps

class ListProductSerializer(generics.ListAPIView):  
    serializer_class = ProductSerializer

    def get_queryset(self): 
        Product = next((m for m in apps.get_models() if m._meta.db_table=='PRODUCT'), None)
        # pprint(model)
        response = Product.objects.all().order_by('id')
        return response 

# class DetailCosmeticsshortnameView(generics.RetrieveUpdateAPIView):
#     serializer_class = DetailCosmeticsshortnameSerializer
#     http_method_names = ['patch','get']

#     def get_queryset(self, *args, **kwargs):
#         qs = Cosmeticsshortname.objects.filter(tradecode=self.kwargs["pk"])
#         return qs
    
#     def patch(self,request, *args, **kwargs):
#         base_response = super(DetailCosmeticsshortnameView, self).patch(request, *args, **kwargs)
#         return base_response
