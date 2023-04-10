from rest_framework import serializers

class AccountItemsEditSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    account_code = serializers.CharField(required=False)

class AccountItemsListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    code = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    user_type_id = serializers.IntegerField(required=False)
