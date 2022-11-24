from pprint import pprint
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cosmeticsshortname
from rest_framework import generics
from .serializers import DetailCosmeticsshortnameSerializer,CosmeticsshortnameSerializer

class ListCosmeticsshortnameView(generics.ListAPIView):  
    serializer_class = DetailCosmeticsshortnameSerializer

    def get_queryset(self): 
        response = Cosmeticsshortname.objects.all().order_by("-id")
        return response 

class CosmeticsshortnameCreate(generics.CreateAPIView):
    queryset = Cosmeticsshortname.objects.all()
    serializer_class = CosmeticsshortnameSerializer

class DetailCosmeticsshortnameView(generics.RetrieveUpdateAPIView):
    serializer_class = DetailCosmeticsshortnameSerializer
    http_method_names = ['patch','get']

    def get_queryset(self, *args, **kwargs):
        qs = Cosmeticsshortname.objects.filter(id=self.kwargs["pk"])
        return qs
    
    def patch(self,request, *args, **kwargs):
        base_response = super(DetailCosmeticsshortnameView, self).patch(request, *args, **kwargs)
        return base_response


class DestoryCosmeticsshortnameView(generics.DestroyAPIView):
    serializer_class = DetailCosmeticsshortnameSerializer

    def delete(self, request, *args, **kwargs):
        base_response = super(DestoryCosmeticsshortnameView, self).delete(request, *args, **kwargs)
        msg = 'Cosmeticsshortname deleted successfully'
        return Response(msg)

    def get_queryset(self, *args, **kwargs):
        qs = Cosmeticsshortname.objects.all()
        return qs