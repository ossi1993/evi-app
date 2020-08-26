from django.urls import include, path
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from ..api import views as ev
# from ..api.views import IndexHTML

router = DefaultRouter()
router.register(r'device', ev.DeviceViewSet)
router.register(r'device-attribute', ev.DeviceAttributeViewSet)
router.register(r'device-template', ev.DeviceTemplateViewSet)
router.register(r'device-template-attribute', ev.DeviceTemplateAttributeViewSet)
router.register(r'inspection', ev.InspectionViewSet)
router.register(r'inspection-template', ev.InspectionTemplateViewSet)
router.register(r'inspection-template-attribute', ev.InspectionTemplateAttributeViewSet)
router.register(r'item', ev.ItemViewSet)
router.register(r'item-attribute', ev.ItemAttributeViewSet)
router.register(r'item-template', ev.ItemTemplateViewSet)
router.register(r'item-template-attribute', ev.ItemTemplateAttributeViewSet)
router.register(r'manufacturer', ev.ManufacturerViewSet)
router.register(r'model', ev.ModelViewSet)
router.register(r'order', ev.OrderViewSet)
router.register(r'order-item', ev.OrderItemViewSet)
router.register(r'order-device', ev.OrderDeviceViewSet)
router.register(r'sample', ev.SampleViewSet)
router.register(r'sample-attribute', ev.SampleAttributeViewSet)
router.register(r'supplier', ev.SupplierViewSet)
router.register(r'inspection-template-list', ev.InspectionTemplateListView)
# router.register(r'device-list', ev.DeviceListView)

urlpatterns = [
    path("", include(router.urls)), 

    # path("item-test/", ev.ItemTestListView.as_view()), 
    path("device-list/", ev.DeviceListView.as_view()), 
    path("model-list/", ev.ModelListView.as_view()), 
    path("item-list/", ev.ItemListView.as_view()), 
    # path("inspection-template-list/", ev.InspectionTemplateListView.as_view()), 
    path("order-list/", ev.OrderListView.as_view()), 
    # path('home/', IndexHTML), 
    #path(r'^$', ev.IndexHTML), 
]