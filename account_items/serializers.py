from rest_framework import serializers
import xmlrpc.client

url = 'http://localhost:8069'
db = '6ou'
username = 'admin@yahoo.com'
password = '6ou_admin1'
# password = env('DATABASE_PASS')
common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


def get_account_types():
        result = models.execute_kw(db, uid, password, 'account.account.type', 'search_read', 
                   [[]], {'fields':["id",'name']})
        return [(d['id'],d['name']) for d in result]


class AccountItemsAddSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    code = serializers.CharField(required=False)
    account_types = serializers.ChoiceField(choices=get_account_types())


class AccountItemsEditSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    account_name = serializers.CharField(required=True)
    

class AccountItemsListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_type_id = serializers.IntegerField(required=False)
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)


class AnalyticAccountList(serializers.Serializer):
    limit =serializers.IntegerField(required=False)
    offset = serializers.IntegerField(required=False)
    search =serializers.CharField(required=False)
