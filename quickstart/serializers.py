from .models import Cosmeticsshortname
from rest_framework import serializers



class CosmeticsshortnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosmeticsshortname
        fields = ('shorttradename', 'company_code','trade_name')



class DetailCosmeticsshortnameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Cosmeticsshortname
        fields = ('tradecode','shorttradename', 'company_code','trade_name')
