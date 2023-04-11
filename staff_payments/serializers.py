from rest_framework import serializers

class EditStaffMemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=False)
    national_id = serializers.CharField(required=False)
