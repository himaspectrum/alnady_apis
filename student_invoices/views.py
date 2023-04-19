from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import CreateStudentInvoiceSerializer,CreateStudentInvoiceLinesSerializer

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



class CreateStudentInvoice(APIView):
    @swagger_auto_schema(
        request_body=CreateStudentInvoiceSerializer,
        responses={201: 'Created'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def post(self,request):
        # serializer = CreateStudentInvoiceLinesSerializer(data=request.data)

        invoice_number = request.query_params.get('invoice_number', None)
        total = request.query_params.get('total', None)
        # account_items = request.query_params.get('account_items', None)
        currency = request.query_params.get('currency', None)
        created_date = request.query_params.get('created_date', None)
        	
        miscellaneous_operations_id = 3
        # try:
        account_id = models.execute_kw(db, uid, password, 'account.move', 'create', [{
        'ref': invoice_number,'currency_id':currency,'journal_id':miscellaneous_operations_id,
        'date':created_date
        }])
        items = []
        for item_data in serializer.validated_data:
            items.append(item_data)
        print(items)
            # models.execute_kw(db, uid, password, 'account.move.line', 'create', [{
            #     'ref': invoice_number,'currency_id':currency,'journal_id':miscellaneous_operations_id,
            #     'date':created_date
            #     }])
        base_total = models.execute_kw(db, uid, password, 'account.move', 'search_read', 
                [[('id', '=',account_id)]], {'fields':["id",'name','amount_total_signed'],})[0]['amount_total_signed']
        if base_total != float(total):
            return Response({'error': 'total are not equal'}, status=500)
        
        # except Exception as e:
        #     return Response({'error': str(e)}, status=500)
        return Response({'result':account_id ,'Status':bool(account_id)})

