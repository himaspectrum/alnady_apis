from rest_framework import serializers

class MyQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    account_code = serializers.CharField(required=False)
