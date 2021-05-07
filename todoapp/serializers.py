from rest_framework import serializers
from todoapp.models import TodoModel

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = '__all__'

class TodoDescriptioniSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id','description']