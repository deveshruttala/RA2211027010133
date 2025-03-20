from rest_framework import serializers
from .models import NumberStore

class NumberStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberStore
        fields = '__all__'