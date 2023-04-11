from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import AccountItemsEditSerializer,AccountItemsListSerializer

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


class AccountItemsEdit(APIView):
    @swagger_auto_schema(
        query_serializer=AccountItemsEditSerializer,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def put(self,request,name=None,account_code=None ):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        _id = request.query_params.get('id', None)
        account_code = request.query_params.get('account_code', None)
        name = request.query_params.get('name', None)

        result = models.execute_kw(db, uid, password, 'account.account', 'search_read', 
                   [[('id', '=',_id)]], {'fields':["code",'name','user_type_id'], 'limit': limit, 'offset': offset})
        result_id = result[0]['id']
        if account_code:
            models.execute_kw(db, uid, password, 'account.account', 'write', [[result_id], {'account_code': account_code}])
        if name:
            models.execute_kw(db, uid, password, 'account.account', 'write', [[result_id], {'name': name}])
        return Response({'result': result})


class AccountItemsList(APIView):
    @swagger_auto_schema(
        query_serializer=AccountItemsListSerializer,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def get(self,request, *args, **kwargs):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        _id = request.query_params.get('id', None)
        user_type_id = request.query_params.get('user_type_id', None)
        code = request.query_params.get('code', None)
        name = request.query_params.get('name', None)
        domain = []
        if _id:
            domain.append(('id', '=',_id))
        if user_type_id:
            domain.append(('user_type_id', '=',user_type_id))
        if code:
            domain.append(('code', '=',code))
        if name:
            domain.append(('name', 'like',name))
        result = models.execute_kw(db, uid, password, 'account.account', 'search_read', 
                   [domain], {'fields':["code",'name','user_type_id'], 'limit': limit, 'offset': offset})
        items_count= len(result)
        
        return Response({'result': result,'items_count':items_count})


class ShowStaffPaymentDetails(APIView):
    def get(self,request, *args, **kwargs):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        payment_id = kwargs['payment_id']

        payslip_details = models.execute_kw(db, uid, password, 'hr.payslip', 'search_read', 
                    [[('id', '=', payment_id)]],
                    {'fields': ['id', 'name', 'net_wage', 'currency_id','line_ids'], 'limit': limit, 'offset': offset})   
        if not payslip_details:
            message = 'payslip not exist'
            return Response({'result': message})


        payslip_lines = models.execute_kw(db, uid, password, 'hr.payslip.line', 'search_read', 
                    [[('slip_id', '=', payslip_details[0]['id'])]],
                )   
        items_count= len(payslip_details)
        payslip_details[0].update({'line_ids':payslip_lines})
        return Response({'result': payslip_details,'items_count':items_count})

