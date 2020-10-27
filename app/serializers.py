from rest_framework import serializers
from .models import Node
class nodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'