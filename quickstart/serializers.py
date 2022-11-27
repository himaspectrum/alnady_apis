from .models import Product,ProductDetails,Tempdrugsmanufacture
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Product
        fields = ('id','english_name')



# class DetailCosmeticsshortnameSerializer(serializers.ModelSerializer):
  
#     class Meta:
#         model = Cosmeticsshortname
#         fields = ('tradecode','shorttradename', 'company_code','trade_name')
