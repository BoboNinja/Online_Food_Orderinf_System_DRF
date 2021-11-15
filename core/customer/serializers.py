from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from customer.models import CustomerAccount, CustomerOrder, CustomerOrderItem

class CustomerAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAccount
        fields ='__all__'

class CustomerOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrder
        fields = '__all__'

class CustomerOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerOrderItem
        fields = '__all__'