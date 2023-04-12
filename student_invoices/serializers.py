from rest_framework import serializers

    

class CreateStudentInvoiceSerializer(serializers.Serializer):
    invoice_number = serializers.CharField(required=True)
    total = serializers.FloatField(required=True)
    account_items = serializers.IntegerField(required=True)
    currency = serializers.IntegerField(required=True)
    journal_id = serializers.IntegerField(required=True)
