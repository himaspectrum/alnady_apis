from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import BankListSerializer

# third party
import environ

env = environ.Env()
environ.Env.read_env()


url = 'http://localhost:8069'
db = '6ou'
username = 'admin@yahoo.com'
password = '6ou_admin1'
# password = env('DATABASE_PASS')
common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))



class BankList(APIView):
    @swagger_auto_schema(
        query_serializer=BankListSerializer,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def get(self,request, *args, **kwargs):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        _id = request.query_params.get('id', None)
        bic = request.query_params.get('bic', None)
        name = request.query_params.get('name', None)
        domain = []
        if _id:
            domain.append(('id', '=',_id))
        if bic:
            domain.append(('bic', '=',bic))
        if name:
            domain.append(('name', 'like',name))
        result = models.execute_kw(db, uid, password, 'res.bank', 'search_read', 
                   [domain], {'fields':["bic",'name','id'], 'limit': limit, 'offset': offset})
        items_count= len(result)
        
        return Response({'result': result,'items_count':items_count})



