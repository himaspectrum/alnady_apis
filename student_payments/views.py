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
        # limit = int(request.query_params.get('limit', 10))
        # offset = int(request.query_params.get('offset', 0))

        _id = request.query_params.get('id', None)
        bic = request.query_params.get('code', None)
        name = request.query_params.get('name', None)
        domain = [('type', "=" , "bank")]
        if _id:
            domain.append(('id', '=',_id))
        if bic:
            domain.append(('code', 'like',bic))
        if name:
            domain.append(('name', 'like',name))
        result = models.execute_kw(db, uid, password, 'account.journal', 'search_read', 
                   [domain],{"fields":["id",'name','code']} )
        items_count= len(result)
        
        return Response({'result': result,'items_count':items_count})


class  StudentInvoiceTransaction(APIView):
    def post(self,request):
        miscellaneous_operations_id=3
        # get lines by invoice numbe/r
        invoice_number = request.data.get('invoice_number')
        account_id = int(request.data.get('account'))
        paid_amount = int(request.data.get('amount'))
        bank_id = int(request.data.get('bank_id'))


        move_id = models.execute_kw(db,uid, password,'account.move','search',[[('ref',"=",invoice_number)]])

        lines  = models.execute_kw(db,uid, password,'account.move.line','search_read',[[("move_id",'=',move_id)]])
        
        # debit_accounts = [line for line in lines if int(line.get('debit'))  >  0]
        # credit_accounts = [line for line in lines if int(line.get('credit'))  >  0]
        journal_entry_data = {
            'journal_id':miscellaneous_operations_id,
            
        }

        cr_move_id = models.execute_kw(db,uid, password,'account.move','create',[journal_entry_data])
        
    
        # pre_depit_account = debit_accounts[0]
        # pre_credit_account = credit_accounts[0]


        #  bank entry
        cr_lines = models.execute_kw(db,uid, password,'account.move.line','create',[{"move_id":cr_move_id,"debit":paid_amount,'account_id':bank_id}],{'context' :{'check_move_validity': False}})
        cr_lines2 = models.execute_kw(db,uid, password,'account.move.line','create',[{"move_id":cr_move_id,"credit":paid_amount,'account_id':account_id}],{'context' :{'check_move_validity': True}})


        # ather entry
        # cr_lines = models.execute_kw(db,uid, password,'account.move.line','create',[{"move_id":cr_move_id,"debit":paid_amount,'account_id':pre_credit_account['account_id'][0]}],{'context' :{'check_move_validity': False}})
        # cr_lines = models.execute_kw(db,uid, password,'account.move.line','create',[{"move_id":cr_move_id,"credit":paid_amount,'account_id':account_id}],{'context' :{'check_move_validity': True}})
        




        return Response({"status":True,"message":{
            "id":cr_move_id
        } })


class StudentInvoiceTransactionRefund(APIView):


    def post(self, request):
        # create journal entry 
        paid_amount =int( request.data.get("amount"))
        account_id =int( request.data.get("account"))
        bank_id = int(request.data.get('bank_id'))

        
        miscellaneous_operations_id=3
        journal_entry_data = {
            'journal_id':miscellaneous_operations_id,
            
        }
        move_id = models.execute_kw(db,uid, password,'account.move','create',[journal_entry_data])
        line = models.execute_kw(db,uid, password,'account.move.line','create',[{"move_id":move_id,"debit":paid_amount,'account_id':account_id}],{'context' :{'check_move_validity': False}})
        line2 = models.execute_kw(db,uid, password,'account.move.line','create',[{"move_id":move_id,"credit":paid_amount,'account_id':bank_id}],{'context' :{'check_move_validity': True}})


        return Response({"result":move_id})