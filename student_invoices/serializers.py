from rest_framework import serializers

    
class CreateStudentInvoiceLinesSerializer(serializers.Serializer):
    debit = serializers.FloatField(required=True)
    credit = serializers.FloatField(required=True)
    currency_id = serializers.IntegerField(required=True)

class CreateStudentInvoiceSerializer(serializers.Serializer):
    invoice_number = serializers.CharField(required=True)
    account_items = CreateStudentInvoiceLinesSerializer(many=True)
    currency = serializers.IntegerField(required=True)
    created_date = serializers.DateTimeField(required=True)

class CancelStudentInvoiceSerializer(serializers.Serializer):
    invoice_number = serializers.IntegerField(required=True)
    # account_items = CreateStudentInvoiceLinesSerializer(many=True)
    currency = serializers.IntegerField(required=True)
    created_date = serializers.DateTimeField(required=True)
