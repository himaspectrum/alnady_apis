from .models import Cosmeticsshortname
from rest_framework import serializers



class CosmeticsshortnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmeticsshortname
        fields = ('tradecode','shorttradename', 'company_code','trade_name')

    def create(self, validated_data):
        product = Cosmeticsshortname(**validated_data)
        product.save()
        return product



class DetailCosmeticsshortnameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Cosmeticsshortname
        fields = ('tradecode','shorttradename', 'company_code','trade_name')
