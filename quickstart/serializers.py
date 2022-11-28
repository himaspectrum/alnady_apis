from .models import Product,ProductDetails,Tempdrugsmanufacture
from rest_framework import serializers



class ProductSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Product
        fields = ('id','notification_no','english_name')



class DetailCosmeticsshortnameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductDetails
        fields = ('id','product_id','fragrance','product_colour', 'flavor')
