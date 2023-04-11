from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

from drf_yasg.utils import swagger_auto_schema
from .serializers import EditStaffMemberSerializer

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

class EditStaffMember(APIView):
    @swagger_auto_schema(
        query_serializer=EditStaffMemberSerializer,
        responses={200: 'Success'},
        operation_summary='My View Summary',
        operation_description='My View Description'
    )
    def put(self,request,name=None,account_code=None ):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))

        _id = request.query_params.get('id', None)
        national_id = request.query_params.get('national_id', None)
        name = request.query_params.get('name', None)

        result = models.execute_kw(db, uid, password, 'hr.employee', 'search_read', 
                   [[('id', '=',_id)]], {'fields':["id",'name'], 'limit': limit, 'offset': offset})
        result_id = result[0]['id']
        if national_id:
            models.execute_kw(db, uid, password, 'hr.employee', 'write', [[result_id], {'identification_id': national_id}])
        if name:
            models.execute_kw(db, uid, password, 'hr.employee', 'write', [[result_id], {'name': name}])
        result = models.execute_kw(db, uid, password, 'hr.employee', 'search_read', 
                   [[('id', '=',_id)]], {'fields':["id",'name','identification_id'], 'limit': limit, 'offset': offset})
        return Response({'result': result})

class StaffPaymentsList(APIView):
    def get(self,request, *args, **kwargs):
        limit = int(request.query_params.get('limit', 10))
        offset = int(request.query_params.get('offset', 0))
        
        identification_id = kwargs['identification_id']

        employee = models.execute_kw(db, uid, password,'hr.employee', 'search_read',
                                     [[('identification_id', '=', identification_id)]],
                                    {'fields': ['id', 'name']})        
        if employee:
            employee_id = employee[0]['id']
        else:
            message = 'employee not exist'
            return Response({'result': message})
        payslip_list = models.execute_kw(db, uid, password, 'hr.payslip', 'search_read', 
                    [[('employee_id', '=', employee_id)]],
                    {'fields': ['id', 'name', 'net_wage', 'currency_id'], 'limit': limit, 'offset': offset})   
        items_count= len(payslip_list)
        return Response({'result': payslip_list,'items_count':items_count})


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

