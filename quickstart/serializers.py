from .models import Product,ProductDetails,ProductBatches
from rest_framework import serializers
from pprint import pprint

class ProductBatchesSerializer(serializers.ModelSerializer):  
    product_id = serializers.IntegerField()     
    lkup_uom_id = serializers.IntegerField()

    

    class Meta:
        model = ProductBatches
        fields = ('product_id','lkup_uom_id')


class ProductSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Product
        fields = ('id','notification_no','english_name')



class DetailCosmeticsshortnameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductDetails
        fields = ('id','product_id','fragrance','product_colour', 'flavor')
