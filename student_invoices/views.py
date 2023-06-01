from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from .serializers import CreateStudentInvoiceSerializer,CreateStudentInvoiceLinesSerializer,CancelStudentInvoiceSerializer,AnalyticItemListSerializer

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

        # journal data 
        journal_entry_data = {
            'ref': invoice_number,
            'journal_id':miscellaneous_operations_id,
            'date':created_date,
            'currency_id':currency,
            
            
        }
        account_move_id = models.execute_kw(db, uid, password, 'account.move', 'create', [journal_entry_data
        ])


        # loop all lines except last one check balnce off
        for item_index in range(0 , len(account_items) -1):
             models.execute_kw(db, uid, password, 'account.move.line', 'create',
                            [{
                            'move_id': account_move_id, 
                            **account_items[item_index]  
                            }],{'context' :{'check_move_validity': False}})

                            # 
        # last entry check balance   on
        models.execute_kw(db, uid, password, 'account.move.line', 'create',
                            [{
                            'move_id': account_move_id, 
                            **account_items[-1]  
                            }],{'context' :{'check_move_validity': True}})
               





        #     models.execute_kw(db, uid, password, 'account.move.line', 'create', [{
        #         'account_id': miscellaneous_operations_id,
        #         'move_id': account_move_id,
        #         **item
        #     }], {'context': {'check_move_validity': False}})
        #     print(item)

        
        # account_move_object = models.execute_kw(db, uid, password, 'account.move', 'search_read', 
        #         [[('id', '=',account_move_id)]], {'fields':["id",'name','amount_total_signed'],})
        # try:
        #     models.execute_kw(db, uid, password, 'account.move', 'action_post', [[account_move_object[0]['id']]])
        # except Exception as e:
        #     return Response({'error': str(e)}, status=500)

        return Response({'result':account_move_id ,'Status':bool(account_move_id)})


class CancelStudentInvoice(APIView):
    @swagger_auto_schema(
        request_body=CancelStudentInvoiceSerializer,
        responses={201: 'Created'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def post(self,request):

        move_id = request.data.get('invoice_number', None)
        # account_items = request.data.get('account_items', None)
        # currency = request.data.get('currency', None)
        created_date = request.data.get('created_date', None)
            
        miscellaneous_operations_id = 3
        
        reversal = models.execute_kw(db, uid, password, 'account.move.reversal', 'create', [{
            'journal_id': miscellaneous_operations_id,
            'date': created_date,
            'move_ids': [(4, move_id)],
        }])

        # reverse the move
        result = models.execute_kw(db, uid, password, 'account.move.reversal', 'reverse_moves', [reversal])
        try:
            models.execute_kw(db, uid, password, 'account.move', 'action_post', [[result['res_id']]])
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'result':result ,'Status':bool(result)})
        ...


class AnalyticItemList(APIView):
    @swagger_auto_schema(
        query_serializer=AnalyticItemListSerializer,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def get(self,request, *args, **kwargs):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))
        

        analytic_item_list = models.execute_kw(db, uid, password, 'account.analytic.line', 'search_read', 
                    [],
                    {'limit': limit, 'offset': offset})   
        items_count= len(analytic_item_list)
        return Response({'result': analytic_item_list,'items_count':items_count})

