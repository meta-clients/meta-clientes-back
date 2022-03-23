from rest_framework import serializers
from ..models import ClientModel, ChildrenModel

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildrenModel
        fields = '__all__'
