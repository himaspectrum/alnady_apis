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

class AccountItemsView(APIView):
    def get(self,request, *args, **kwargs):
        result = models.execute_kw(db, uid, password, 'account.account', 'search_read', 
                   [], {'fields':["code",'name','user_type_id']})
        return Response({'result': result})

