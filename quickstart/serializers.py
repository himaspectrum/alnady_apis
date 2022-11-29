from .models import Product,ProductDetails,ProductBatches
from rest_framework import serializers
from pprint import pprint

class ProductBatchesSerializer(serializers.ModelSerializer):  
    product_id = serializers.IntegerField()     
    lkup_uom_id = serializers.IntegerField()

    
    def validate_product_id(self, value):
        product_object =Product.objects.filter(id=value)
        if not product_object.exists():
            raise serializers.ValidationError("this product id is not exist")
        return value

    def validate_lkup_uom_id(self, value):
        lkup_object =ProductBatches.objects.filter(id=value)
        if not lkup_object.exists():
            raise serializers.ValidationError("this object id is not exist")
        return value
    class Meta:
        model = ProductBatches
        fields = ('product_id','lkup_uom_id','batch_no')


class ProductSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Product
        fields = ('id','notification_no','english_name')



class DetailCosmeticsshortnameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductDetails
        fields = ('id','product_id','fragrance','product_colour', 'flavor')
