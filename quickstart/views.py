from pprint import pprint
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Inventory

class TestView(APIView):
    def get(self,request, *args, **kwargs):
        result = Inventory.objects.all().values()
        pprint(type(result  ))
        pprint(f'{result=}')
        return Response({'result': result})