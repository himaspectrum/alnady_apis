from pprint import pprint
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
password = env('DATABASE_PASS')






# info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
# url, db, username, password = info['host'], info['database'], info['user'], info['password']
# common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

class TestView(APIView):
    def get(self,request, *args, **kwargs):
        result = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]])
        pprint(result)
        return Response({'result': result})

