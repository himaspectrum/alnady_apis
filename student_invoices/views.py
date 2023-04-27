from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import CreateStudentInvoiceSerializer,CreateStudentInvoiceLinesSerializer,CancelStudentInvoiceSerializer

# third party
import environ
from rest_framework.parsers import MultiPartParser

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
models.allow_none = True


class CreateStudentInvoice(APIView):
    @swagger_auto_schema(
        request_body=CreateStudentInvoiceSerializer,
        responses={201: 'Created'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def post(self,request):

        invoice_number = request.data.get('invoice_number', None)
        account_items = request.data.get('account_items', None)
        currency = request.data.get('currency', None)
        created_date = request.data.get('created_date', None)
        	
        miscellaneous_operations_id = 3
        # try:
        account_move_id = models.execute_kw(db, uid, password, 'account.move', 'create', [{
        'ref': invoice_number,'currency_id':currency,'journal_id':miscellaneous_operations_id,
        'date':created_date
        }])
        for item in account_items:
            models.execute_kw(db, uid, password, 'account.move.line', 'create', [{
                'account_id': miscellaneous_operations_id,
                'move_id': account_move_id,
                **item
            }], {'context': {'check_move_validity': False}})

        
        account_move_object = models.execute_kw(db, uid, password, 'account.move', 'search_read', 
                [[('id', '=',account_move_id)]], {'fields':["id",'name','amount_total_signed'],})
        try:
            models.execute_kw(db, uid, password, 'account.move', 'action_post', [[account_move_object[0]['id']]])
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'result':account_move_id ,'Status':bool(account_move_id)})


class CancelStudentInvoice(APIView):
    @swagger_auto_schema(
        request_body=CancelStudentInvoiceSerializer,
        responses={201: 'Created'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def post(self,request):

        # invoice_number = request.data.get('invoice_number', None)
        # account_items = request.data.get('account_items', None)
        # currency = request.data.get('currency', None)
        # created_date = request.data.get('created_date', None)
            
        # miscellaneous_operations_id = 3
        
        # result=None        

        # models.execute_kw(db, uid, password, 'account.move', 'button_cancel', [int(invoice_number)])
        # return Response({'result':result ,'Status':bool(result)})
        ...
