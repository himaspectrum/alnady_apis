from rest_framework import serializers

    

class BankListSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    bic = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
