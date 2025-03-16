from rest_framework import serializers

class QuotationSerializer(serializers.Serializer):
    rooms = serializers.IntegerField(min_value=1)
    sockets = serializers.IntegerField(min_value=1)
    lights = serializers.IntegerField(min_value=0)
    phases = serializers.IntegerField(min_value=1)
    has_washing_machine = serializers.BooleanField(default=False)
    has_induction = serializers.BooleanField(default=False)
    has_fridge = serializers.BooleanField(default=False)
    has_dryer = serializers.BooleanField(default=False)
