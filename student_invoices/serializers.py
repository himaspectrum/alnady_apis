from rest_framework import serializers

    
class CreateStudentInvoiceLinesSerializer(serializers.Serializer):
    account_id = serializers.CharField(required=True)
    debit = serializers.FloatField(required=True)
    credit = serializers.FloatField(required=True)
    currency = serializers.IntegerField(required=True)

class CreateStudentInvoiceSerializer(serializers.Serializer):
    invoice_number = serializers.CharField(required=True)
    total = serializers.FloatField(required=True)
    account_items = CreateStudentInvoiceLinesSerializer(many=True)
    currency = serializers.IntegerField(required=True)
    created_date = serializers.DateTimeField(required=True)
