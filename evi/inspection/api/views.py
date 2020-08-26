from django.db.models import F, Prefetch
from django.db.models.query import prefetch_related_objects
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from rest_framework import generics, status, viewsets, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django import db

from ..models import (Device, DeviceTemplate, DeviceTemplateAttribute,
                     Inspection, InspectionTemplate,
                     InspectionTemplateAttribute, Item, ItemAttribute,
                     ItemTemplate, ItemTemplateAttribute, Manufacturer, Model,
                     DeviceAttribute, OrderDevice, Order, OrderItem, Sample,
                     SampleAttribute, Supplier)
from .serializers import (DeviceAttributeSerializer, OrderDeviceSerializer,
                          DeviceTemplateSerializer, DeviceTemplateAttributeSerializer,
                          InspectionSerializer, InspectionTemplateSerializer,
                          InspectionTemplateAttributeSerializer, ItemSerializer,
                          ItemAttributeSerializer, ItemTemplateSerializer,
                          ItemTemplateAttributeSerializer, ManufacturerSerializer,
                          DeviceSerializer, ModelSerializer, OrderSerializer,
                          OrderItemSerializer, SampleSerializer,
                          SampleAttributeSerializer, SupplierSerializer,
                          NewDeviceSerializer, ItemDeviceSerializer, DeviceListSerializer,
                          ModelListSerializer, ItemListSerializer, InspectionTemplateListSerializer,
                          OrderListSerializer)


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by("txtSerialNumber")
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceAttributeViewSet(viewsets.ModelViewSet):
    queryset = DeviceAttribute.objects.all().order_by("txtKeyAttribute")
    serializer_class = DeviceAttributeSerializer
    permission_classes = [IsAuthenticated]


class OrderDeviceViewSet(viewsets.ModelViewSet):
    queryset = OrderDevice.objects.all().order_by("-datOrder")
    serializer_class = OrderDeviceSerializer
    permission_classes = [IsAuthenticated]


class DeviceTemplateViewSet(viewsets.ModelViewSet):
    queryset = DeviceTemplate.objects.all()
    serializer_class = DeviceTemplateSerializer
    permission_classes = [IsAuthenticated]


class DeviceTemplateAttributeViewSet(viewsets.ModelViewSet):
    queryset = DeviceTemplateAttribute.objects.all().order_by("txtKeyAttribute")
    serializer_class = DeviceTemplateAttributeSerializer
    permission_classes = [IsAuthenticated]


class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all().order_by("txtInspectionNumber")
    serializer_class = InspectionSerializer
    permission_classes = [IsAuthenticated]


class InspectionTemplateViewSet(viewsets.ModelViewSet):
    queryset = InspectionTemplate.objects.all().order_by("txtInspectionTemplateName")
    serializer_class = InspectionTemplateSerializer
    permission_classes = [IsAuthenticated]


class InspectionTemplateAttributeViewSet(viewsets.ModelViewSet):
    queryset = InspectionTemplateAttribute.objects.all().order_by("txtKeyAttribute")
    serializer_class = InspectionTemplateAttributeSerializer
    permission_classes = [IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by("txtArticlenumber")
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class ItemAttributeViewSet(viewsets.ModelViewSet):
    queryset = ItemAttribute.objects.all().order_by("txtKeyAttribute")
    serializer_class = ItemAttributeSerializer
    permission_classes = [IsAuthenticated]


class ItemTemplateViewSet(viewsets.ModelViewSet):
    queryset = ItemTemplate.objects.all()
    serializer_class = ItemTemplateSerializer
    permission_classes = [IsAuthenticated]


class ItemTemplateAttributeViewSet(viewsets.ModelViewSet):
    queryset = ItemTemplateAttribute.objects.all().order_by("txtKeyAttribute")
    serializer_class = ItemTemplateAttributeSerializer
    permission_classes = [IsAuthenticated]


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by("txtManufacturerName")
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all().order_by("txtModelName")
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-datOrder")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = [IsAuthenticated]


class SampleAttributeViewSet(viewsets.ModelViewSet):
    queryset = SampleAttribute.objects.all().order_by("txtKeyAttribute")
    serializer_class = SampleAttributeSerializer
    permission_classes = [IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by("txtSupplierName")
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class DeviceListView(generics.ListAPIView):
    queryset = Device.objects.all().select_related('idModel')
    serializer_class = DeviceListSerializer
    permission_classes = [IsAuthenticated]


class ModelListView(generics.ListAPIView):
    queryset = Model.objects.all().select_related('idManufacturer')
    serializer_class = ModelListSerializer
    permission_classes = [IsAuthenticated]


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [IsAuthenticated]


class InspectionTemplateListView(viewsets.ModelViewSet):
    queryset = InspectionTemplate.objects.all()
    serializer_class = InspectionTemplateListSerializer
    permission_classes = [IsAuthenticated]


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]













# how to - https://stackoverflow.com/questions/50824230/django-query-multi-level-foreign-keys
# class ItemTestListView(generics.ListAPIView):

#     serializer_class = ItemDeviceSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'item_list.html'

#     def get(self, request):
#         ds = Model.objects.all()
#         # prefetch = Prefetch('idModel_set', queryset=Item.objects.all())
#         # data = Item.objects.all().prefetch_related(prefetch)
#         queryset = Item.objects.annotate(model_name=F('deviceModels__txtModelName'),
#                                         device_name=F('deviceModels__idDevice__txtDeviceName'),
#                                         manufacturer_name=F('deviceModels__idDevice__idManufacturer__txtManufacturerName'),
#                                         supplier_name=F('deviceModels__idDevice__idSupplier__txtSupplierName'))

#         dataset = Item.objects.all().prefetch_related('deviceModels')
#         for data in dataset:
#             print(data.deviceModels.txtModelName)
#         print(dataset.query)

#         return Response({'items': dataset})


# class DeviceListView(generics.ListAPIView):

#     serializer_class = DeviceModelSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'device_list.html'

#     def get(self, request):
#         queryset = Model.objects.select_related()
#         print(queryset.query)
#         return Response({'devices': queryset})


# def IndexHTML(request):

#     dataset = Item.objects.all().prefetch_related(Prefetch('deviceModels'))

#     package = []

#     for data in dataset:
#         print(data.deviceModels.all())
#         package.append(data.deviceModels.all())
#         print(package)

#     context = {
#         'items': dataset,
#         'models': package,
#         }
#     return render(request, 'index.html', context)
