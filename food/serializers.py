from rest_framework import serializers
from .models import listing

class LagSer(serializers.ModelSerializer):
    class Meta:
        model = listing
        fields =('id', 'title', 'price')