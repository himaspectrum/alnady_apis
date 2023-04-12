from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import CreateStudentInvoiceSerializer

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



class CreateStudentInvoice(APIView):
    @swagger_auto_schema(
        query_serializer=CreateStudentInvoiceSerializer,
        responses={201: 'Created'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def post(self,request):
        invoice_number = request.query_params.get('invoice_number', None)
        total = request.query_params.get('total', None)
        account_items = request.query_params.get('account_items', None)
        currency = request.query_params.get('currency', None)
        journal_id = request.query_params.get('journal_id', None)
        try:
            account_id = models.execute_kw(db, uid, password, 'account.move', 'create', [{
            'ref': invoice_number,'currency_id':currency,'journal_id':journal_id
            }])
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        return Response({'result':account_id ,'Status':bool(account_id)})

