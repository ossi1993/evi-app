from django.contrib import admin

from .models import (Device, DeviceTemplate, DeviceTemplateAttribute,
                     Inspection, InspectionTemplate,
                     InspectionTemplateAttribute, Item, ItemAttribute,
                     ItemTemplate, ItemTemplateAttribute, Manufacturer, Model,
                     DeviceAttribute, OrderDevice, Order, OrderItem, Sample,
                     SampleAttribute, Supplier)

admin.site.register(Device)
admin.site.register(DeviceTemplate)
admin.site.register(DeviceTemplateAttribute)
admin.site.register(Inspection)
admin.site.register(InspectionTemplate)
admin.site.register(InspectionTemplateAttribute)
admin.site.register(Item)
admin.site.register(ItemAttribute)
admin.site.register(ItemTemplate)
admin.site.register(ItemTemplateAttribute)
admin.site.register(Manufacturer)
admin.site.register(Model)
admin.site.register(DeviceAttribute)
admin.site.register(OrderDevice)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Sample)
admin.site.register(SampleAttribute)
admin.site.register(Supplier)
