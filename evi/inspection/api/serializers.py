from rest_framework import serializers
from ..models import (Device, DeviceTemplate, DeviceTemplateAttribute,
                     Inspection, InspectionTemplate,
                     InspectionTemplateAttribute, Item, ItemAttribute,
                     ItemTemplate, ItemTemplateAttribute, Manufacturer, Model,
                     DeviceAttribute, OrderDevice, Order, OrderItem, Sample,
                     SampleAttribute, Supplier)


class DeviceAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceAttribute
        fields = "__all__"


class OrderDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDevice
        fields = "__all__"


class DeviceTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceTemplate
        fields = "__all__"


class DeviceTemplateAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceTemplateAttribute
        fields = "__all__"


class InspectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inspection
        fields = "__all__"


class InspectionTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InspectionTemplate
        fields = "__all__"


class InspectionTemplateAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = InspectionTemplateAttribute
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"


class ItemAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemAttribute
        fields = "__all__"


class ItemTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemTemplate
        fields = "__all__"


class ItemTemplateAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemTemplateAttribute
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = "__all__"


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"


class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = "__all__"


class SampleAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SampleAttribute
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = "__all__"


class NewDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class ItemDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class DeviceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'
        depth = 3


class ModelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = '__all__'
        depth = 1

class ItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"
        depth = 3


class InspectionTemplateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = InspectionTemplate
        fields = "__all__"
        depth = 3


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
        depth = 1
