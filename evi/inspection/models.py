from django.db import models


class Supplier(models.Model):
    txtSupplierName = models.CharField(max_length=240, unique=True)
    txtStreet1 = models.CharField(max_length=120, blank=True, null=True)
    txtStreet2 = models.CharField(max_length=120, blank=True, null=True)
    txtStreet3 = models.CharField(max_length=120, blank=True, null=True)
    txtZip = models.CharField(max_length=60, blank=True, null=True)
    txtCity = models.CharField(max_length=120, blank=True, null=True)
    txtProvince = models.CharField(max_length=120, blank=True, null=True)
    txtLand = models.CharField(max_length=120)
    txtContactPerson = models.CharField(max_length=120, blank=True, null=True)
    txtCpPhone = models.CharField(max_length=60, blank=True, null=True)
    txtCpMail = models.EmailField(blank=True, null=True)
    txtCpSkype = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        ordering = ['txtSupplierName']

    def __str__(self):
        return f'{ self.txtSupplierName } - { self.txtLand }'


class Manufacturer(models.Model):
    txtManufacturerName = models.CharField(max_length=120, unique=True)

    class Meta:
        ordering = ['txtManufacturerName']

    def __str__(self):
        return self.txtManufacturerName


class Model(models.Model):
    idManufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    idSupplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    txtModelName = models.CharField(max_length=120, unique=True)

    class Meta:
        ordering = ['txtModelName']

    def __str__(self):
        return f'{ self.txtModelName } // { self.idManufacturer }'


class Device(models.Model):
    idModel = models.ForeignKey(Model, on_delete=models.CASCADE)
    txtSerialNumber = models.CharField(max_length=120, unique=True)
    txtDevicePosition = models.CharField(max_length=100)

    class Meta:
        ordering = ['txtSerialNumber']

    def __str__(self):
        return f'{ self.txtSerialNumber }'


class DeviceAttribute(models.Model):
    idDevice = models.ForeignKey(Device, on_delete=models.CASCADE)
    txtKeyAttribute = models.CharField(max_length=60)
    txtNameAttribute = models.CharField(max_length=60)
    txtValueAttribute = models.CharField(max_length=120)
    txtValueType = models.CharField(max_length=60)
    txtMeasureUnit = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ['txtKeyAttribute']

    def __str__(self):
        if (self.txtMeasureUnit):   
            return f'{ self.txtKeyAttribute } - { self.txtNameAttribute } - { self.txtValueAttribute } { self.txtMeasureUnit }'
        else:
            return f'{ self.txtKeyAttribute } - { self.txtNameAttribute } - { self.txtValueAttribute }'


class Order(models.Model):
    idSupplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    txtOrderNumber = models.CharField(max_length=120, unique=True)
    datOrder = models.DateField()
    datDelivery = models.DateField(blank=True, null=True)
    txtOrderType = models.CharField(max_length=60)
    txtChargeNumber = models.CharField(max_length=120, blank=True, null=True)
    txtDeliveryStatus = models.CharField(max_length=120)

    def __str__(self):
        return f'{ self.txtOrderNumber }, { self.txtOrderType }  - { self.datOrder }'


class OrderDevice(models.Model):
    idDevice = models.ForeignKey(Device, on_delete=models.CASCADE)
    idSupplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE)
    datOrder = models.DateField()
    datDelivery = models.DateField()
    numOrderAmount = models.PositiveIntegerField()
    txtOrderType = models.CharField(max_length=120)

    class Meta:
        ordering = ['datOrder']


class DeviceTemplateAttribute(models.Model):
    txtKeyAttribute = models.CharField(max_length=60, unique=True)
    txtNameAttribute = models.CharField(max_length=60)
    txtValueDefault = models.CharField(max_length=60)
    txtValueType = models.CharField(max_length=60)
    txtMeasureUnit = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f'{ self.txtKeyAttribute } - { self.txtNameAttribute }'


class DeviceTemplate(models.Model):
    idDeviceTemplateAttribute = models.ManyToManyField(DeviceTemplateAttribute)
    txtDeviceTemplateName = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.txtDeviceTemplateName


class Inspection(models.Model):
    idOrderDevice = models.ForeignKey(OrderDevice, on_delete=models.CASCADE)
    txtInspectionNumber = models.CharField(max_length=120)
    txtInspectionStatus = models.CharField(max_length=120)
    txtInspectionType = models.CharField(max_length=120)
    datInspection = models.DateField(max_length=120)
    txtInspector = models.CharField(max_length=120)
    txtApproval = models.CharField(max_length=120)
    txtComment1 = models.TextField(blank=True, null=True)
    txtComment2 = models.TextField(blank=True, null=True)

    class Meta: 
        unique_together = ['txtInspectionNumber', 'txtInspectionType']

    def __str__(self):
        return f'{ self.txtInspectionType } - { self.txtInspectionNumber }'


class InspectionTemplateAttribute(models.Model):
    txtItemType = models.CharField(max_length=100)
    txtKeyAttribute = models.CharField(max_length=60, unique=True)
    txtNameAttribute = models.CharField(max_length=60)
    txtValueDefault = models.CharField(max_length=60)
    txtValueType = models.CharField(max_length=60)
    txtMeasureUnit = models.CharField(max_length=60, blank=True, null=True)
    txtValueMin = models.CharField(max_length=60, blank=True, null=True)
    txtValueMax = models.CharField(max_length=60, blank=True, null=True)
    txtValueTolerance = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ['txtNameAttribute']

    def __str__(self):
        return f'{ self.txtItemType } // { self.txtKeyAttribute } - { self.txtNameAttribute }'


class InspectionTemplate(models.Model):
    idInspectionTemplateAttribute = models.ManyToManyField(InspectionTemplateAttribute)
    txtInspectionTemplateName = models.CharField(max_length=250, unique=True)
    txtInspectionTemplateType = models.CharField(max_length=60)

    def __str__(self):
        return f'{ self.txtInspectionTemplateType } - { self.txtInspectionTemplateName }'


class Item(models.Model):
    deviceModels = models.ManyToManyField(Model)
    txtArticlenumber = models.CharField(max_length=120, unique=True)
    txtDescription = models.CharField(max_length=240)
    txtType = models.CharField(max_length=120)
    txtVersion = models.CharField(max_length=60)
    curCost = models.FloatField(blank=True, null=True)
    txtGtinEan = models.CharField(max_length=120, blank=True, null=True)
    txtOutline = models.CharField(max_length=60)
    txtLink = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f'{ self.txtArticlenumber } - { self.txtDescription }'


class ItemAttribute(models.Model):
    idItem = models.ForeignKey(Item, on_delete=models.CASCADE)
    txtKeyAttribute = models.CharField(max_length=60)
    txtNameAttribute = models.CharField(max_length=60)
    txtValueAttribute = models.CharField(max_length=60)
    txtValueType = models.CharField(max_length=60)
    txtMeasureUnit = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ['txtKeyAttribute']

    def __str__(self):
        return f'{ self.txtKeyAttribute } - { self.txtNameAttribute }'


class ItemTemplateAttribute(models.Model):
    txtKeyAttribute = models.CharField(max_length=60, unique=True)
    txtNameAttribute = models.CharField(max_length=60)
    txtValueDefault = models.CharField(max_length=60)
    txtValueType = models.CharField(max_length=60)
    txtMeasureUnit = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f'{ self.txtKeyAttribute } - { self.txtNameAttribute }'


class ItemTemplate(models.Model):
    idItemTemplateAttribute = models.ManyToManyField(ItemTemplateAttribute)
    txtItemTemplateName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.txtItemTemplateName


class OrderItem(models.Model):
    idItem = models.ForeignKey(Item, on_delete=models.CASCADE)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE)
    numOrderAmount = models.PositiveIntegerField()


class Sample(models.Model):
    idInspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    idOrderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)


class SampleAttribute(models.Model):
    idSample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    txtKeyAttribute = models.CharField(max_length=60)
    txtNameAttribute = models.CharField(max_length=60)
    txtValueAttribute = models.CharField(max_length=60)
    txtValueType = models.CharField(max_length=60)
    txtMeasureUnit = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        ordering = ['txtKeyAttribute']

    def __str__(self):
        return f'{ self.txtKeyAttribute } - { self.txtNameAttribute }'

