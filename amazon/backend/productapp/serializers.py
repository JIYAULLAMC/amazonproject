from rest_framework import serializers
from productapp.models import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"