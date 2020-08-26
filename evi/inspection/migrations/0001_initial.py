# Generated by Django 3.1 on 2020-08-23 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtSerialNumber', models.CharField(max_length=120, unique=True)),
                ('txtDevicePosition', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['txtSerialNumber'],
            },
        ),
        migrations.CreateModel(
            name='DeviceTemplateAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtKeyAttribute', models.CharField(max_length=60, unique=True)),
                ('txtNameAttribute', models.CharField(max_length=60)),
                ('txtValueDefault', models.CharField(max_length=60)),
                ('txtValueType', models.CharField(max_length=60)),
                ('txtMeasureUnit', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtInspectionNumber', models.CharField(max_length=120)),
                ('txtInspectionStatus', models.CharField(max_length=120)),
                ('txtInspectionType', models.CharField(max_length=120)),
                ('datInspection', models.DateField(max_length=120)),
                ('txtInspector', models.CharField(max_length=120)),
                ('txtApproval', models.CharField(max_length=120)),
                ('txtComment1', models.TextField(blank=True, null=True)),
                ('txtComment2', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InspectionTemplateAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtItemType', models.CharField(max_length=100)),
                ('txtKeyAttribute', models.CharField(max_length=60, unique=True)),
                ('txtNameAttribute', models.CharField(max_length=60)),
                ('txtValueDefault', models.CharField(max_length=60)),
                ('txtValueType', models.CharField(max_length=60)),
                ('txtMeasureUnit', models.CharField(blank=True, max_length=60, null=True)),
                ('txtValueMin', models.CharField(max_length=60)),
                ('txtValueMax', models.CharField(max_length=60)),
                ('txtValueTolerance', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtArticlenumber', models.CharField(max_length=120, unique=True)),
                ('txtDescription', models.CharField(max_length=240)),
                ('txtType', models.CharField(max_length=120)),
                ('txtVersion', models.CharField(max_length=60)),
                ('curCost', models.FloatField(blank=True, null=True)),
                ('txtGtinEan', models.CharField(blank=True, max_length=120, null=True)),
                ('txtOutline', models.CharField(max_length=60)),
                ('txtLink', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTemplateAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtKeyAttribute', models.CharField(max_length=60, unique=True)),
                ('txtNameAttribute', models.CharField(max_length=60)),
                ('txtValueDefault', models.CharField(max_length=60)),
                ('txtValueType', models.CharField(max_length=60)),
                ('txtMeasureUnit', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtManufacturerName', models.CharField(max_length=120, unique=True)),
            ],
            options={
                'ordering': ['txtManufacturerName'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtOrderNumber', models.CharField(max_length=120, unique=True)),
                ('datOrder', models.DateField()),
                ('datDelivery', models.DateField(blank=True, null=True)),
                ('txtOrderType', models.CharField(max_length=60)),
                ('txtChargeNumber', models.CharField(blank=True, max_length=120, null=True)),
                ('txtDeliveryStatus', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numOrderAmount', models.PositiveIntegerField()),
                ('idItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.item')),
                ('idOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.order')),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idInspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.inspection')),
                ('idOrderItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtSupplierName', models.CharField(max_length=240, unique=True)),
                ('txtStreet1', models.CharField(blank=True, max_length=120, null=True)),
                ('txtStreet2', models.CharField(blank=True, max_length=120, null=True)),
                ('txtStreet3', models.CharField(blank=True, max_length=120, null=True)),
                ('txtZip', models.CharField(blank=True, max_length=60, null=True)),
                ('txtCity', models.CharField(blank=True, max_length=120, null=True)),
                ('txtProvince', models.CharField(blank=True, max_length=120, null=True)),
                ('txtLand', models.CharField(max_length=120)),
                ('txtContactPerson', models.CharField(blank=True, max_length=120, null=True)),
                ('txtCpPhone', models.CharField(blank=True, max_length=60, null=True)),
                ('txtCpMail', models.EmailField(blank=True, max_length=254, null=True)),
                ('txtCpSkype', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'ordering': ['txtSupplierName'],
            },
        ),
        migrations.CreateModel(
            name='SampleAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtKeyAttribute', models.CharField(max_length=60)),
                ('txtNameAttribute', models.CharField(max_length=60)),
                ('txtValueAttribute', models.CharField(max_length=60)),
                ('txtValueType', models.CharField(max_length=60)),
                ('txtMeasureUnit', models.CharField(blank=True, max_length=60, null=True)),
                ('idSample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.sample')),
            ],
            options={
                'ordering': ['txtKeyAttribute'],
            },
        ),
        migrations.CreateModel(
            name='OrderDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datOrder', models.DateField()),
                ('datDelivery', models.DateField()),
                ('numOrderAmount', models.PositiveIntegerField()),
                ('txtOrderType', models.CharField(max_length=120)),
                ('idDevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.device')),
                ('idOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.order')),
                ('idSupplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.supplier')),
            ],
            options={
                'ordering': ['datOrder'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='idSupplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.supplier'),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtModelName', models.CharField(max_length=120, unique=True)),
                ('idManufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.manufacturer')),
                ('idSupplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.supplier')),
            ],
            options={
                'ordering': ['txtModelName'],
            },
        ),
        migrations.CreateModel(
            name='ItemTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtItemTemplateName', models.CharField(max_length=100, unique=True)),
                ('idItemTemplateAttribute', models.ManyToManyField(to='inspection.ItemTemplateAttribute')),
            ],
        ),
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtKeyAttribute', models.CharField(max_length=60)),
                ('txtNameAttribute', models.CharField(max_length=60)),
                ('txtValueAttribute', models.CharField(max_length=60)),
                ('txtValueType', models.CharField(max_length=60)),
                ('txtMeasureUnit', models.CharField(blank=True, max_length=60, null=True)),
                ('idItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.item')),
            ],
            options={
                'ordering': ['txtKeyAttribute'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='deviceModels',
            field=models.ManyToManyField(to='inspection.Model'),
        ),
        migrations.CreateModel(
            name='InspectionTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtInspectionTemplateName', models.CharField(max_length=250, unique=True)),
                ('txtInspectionTemplateType', models.CharField(max_length=60)),
                ('idInspectionTemplateAttribute', models.ManyToManyField(to='inspection.InspectionTemplateAttribute')),
            ],
        ),
        migrations.AddField(
            model_name='inspection',
            name='idOrderDevice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.orderdevice'),
        ),
        migrations.CreateModel(
            name='DeviceTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtDeviceTemplateName', models.CharField(max_length=60, unique=True)),
                ('idDeviceTemplateAttribute', models.ManyToManyField(to='inspection.DeviceTemplateAttribute')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtKeyAttribute', models.CharField(max_length=60)),
                ('txtNameAttribute', models.CharField(max_length=60)),
                ('txtValueAttribute', models.CharField(max_length=120)),
                ('txtValueType', models.CharField(max_length=60)),
                ('txtMeasureUnit', models.CharField(blank=True, max_length=60, null=True)),
                ('idDevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.device')),
            ],
            options={
                'ordering': ['txtKeyAttribute'],
            },
        ),
        migrations.AddField(
            model_name='device',
            name='idModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspection.model'),
        ),
        migrations.AlterUniqueTogether(
            name='inspection',
            unique_together={('txtInspectionNumber', 'txtInspectionType')},
        ),
    ]
