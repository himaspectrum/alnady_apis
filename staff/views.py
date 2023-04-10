from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import xmlrpc.client

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

