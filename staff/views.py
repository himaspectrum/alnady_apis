from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

import xmlrpc.client


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

class HrPayslipView(APIView):
    def get(self,request, *args, **kwargs):
        payslip_list = models.execute_kw(db, uid, password, 'hr.payslip', 'search_read', 
                   [], {'fields':["employee_id",'id','line_ids','net_wage']})
        print(f'{payslip_list=}')
        result = True
        return Response({'result': payslip_list})

