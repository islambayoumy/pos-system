from rest_framework import serializers
from .models import Items, Receipt, Receipts_Items

class ItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Items
        fields = (
            'id',
            'code',
            'name',
            'price',
            'stock_amount'
        )

class ReceiptsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receipt
        fields = '__all__'

class ReceiptsItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receipts_Items
        fields = (
            'receipt',
            'item',
            'total_item_amount',
            'paid_amount_per_item'
        )

