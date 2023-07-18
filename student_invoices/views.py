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
        print("____________________here ")
        invoice_number = request.data.get('invoice_number', None)
        account_items = request.data.get('account_items', None)
        currency = request.data.get('currency', None)
        created_date = request.data.get('created_date', None)
        	
    #    check_account_itmem_before 
        ref =account_move_object = models.execute_kw(db, uid, password, 'account.move', 'search', 
                [[('invoice_number', '=',invoice_number)]], )
        if ref :
            return Response({'invoice_number already exist with same name'} , status=500)


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
               

        

        # post created journal 
        account_move_object = models.execute_kw(db, uid, password, 'account.move', 'search_read', 
                [[('id', '=',account_move_id)]], {'fields':["id",'name','amount_total_signed'],})
        try:
            models.execute_kw(db, uid, password, 'account.move', 'action_post', [[account_move_object[0]['id']]])
        except Exception as e:
            return Response({'error': str(e)}, status=500)

        return Response({'result':account_move_id ,'Status':bool(account_move_id)})


class CancelStudentInvoice(APIView):
   
    def post(self,request):
        invoice_number = request.data.get('invoice_number', None)
        account_items = request.data.get('account_items', None)
        created_date = request.data.get('created_date', None)
        currency = request.data.get('currency', None)

        # search by reference 
        move_ids = models.execute_kw(db,uid, password,'account.move','search',[[['ref','=',invoice_number]]])
        if not move_ids:

            return Response({"message":'cant find invoice number'},status=404 ) 
        # reverse journal 
        miscellaneous_operations_id = 3
        reversal = models.execute_kw(db, uid, password, 'account.move.reversal', 'create', [{
            'journal_id': miscellaneous_operations_id,
            'date': created_date,
            'move_ids': [(4, move_ids[0])],
        }])
        return Response({'result':reversal , 'message':bool(reversal)})



        














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

