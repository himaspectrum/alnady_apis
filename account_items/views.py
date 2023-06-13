from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import AccountItemsEditSerializer,AccountItemsListSerializer,AccountItemsAddSerializer ,AnalyticAccountList

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


class AccountItems(APIView):
    @swagger_auto_schema(
        query_serializer=AccountItemsAddSerializer,
        responses={201: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    # account item create 
    def post(self,request):
        code = request.data.get('code', None)
        name = request.data.get('name', None)
        account_types = int(request.data.get('account_types', None))
        try:
            account_id = models.execute_kw(db, uid, password, 'account.account', 'create', [{
            'code': code,'name':name,'user_type_id':account_types
            }])
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'result':account_id ,'Status':bool(account_id)})


    @swagger_auto_schema(
        query_serializer=AccountItemsEditSerializer,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    # update account item
    def put(self,request,name=None,account_code=None ):
        limit = int(request.data.get('limit', 10))
        offset = int(request.data.get('offset', 0))

        _id = request.data.get('id', None)
        account_code = request.data.get('account_code', None)
        name = request.data.get('name', None)

        result = models.execute_kw(db, uid, password, 'account.account', 'search_read', 
                   [[('id', '=',_id)]], {'fields':["code",'name','user_type_id'], 'limit': limit, 'offset': offset})
        result_id = result[0]['id']
        if account_code:
          re1=  models.execute_kw(db, uid, password, 'account.account', 'write', [[result_id], {'account_code': account_code}])
        if name:
           re1 =  models.execute_kw(db, uid, password, 'account.account', 'write', [[result_id], {'name': name}])

        final_result = models.execute_kw(db, uid, password, 'account.account', 'search_read', 
                   [[('id', '=',_id)]],{'fields':["code",'name','user_type_id']} )
        return Response({'result': final_result})


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




class AnalyticitemList(APIView):

    @swagger_auto_schema(
        query_serializer=AnalyticAccountList,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def get(self,request, *args, **kwargs):
        print(request.query_params)
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))
        search_word = request.query_params.get('search',"")
        print("hello there ",search_word)
        print("hello there ",limit)
        print("hello there ",offset)
        analytic_items = models.execute_kw(db,uid , password ,'account.account','search_read',[[('name' , 'like' , search_word)]],{'fields':["id",'name'],'limit': limit, 'offset': offset})
        item_count = len(analytic_items)
        return Response({'count':item_count,'items':analytic_items})

