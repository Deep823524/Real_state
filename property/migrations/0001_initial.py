# Generated by Django 2.1.5 on 2019-03-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_uploaded_date', models.DateField(default=True)),
                ('property_sale_date', models.DateField(default=True)),
                ('property_deleted_date', models.DateField(default=True)),
                ('property_modify_date', models.DateField(default=False)),
                ('property_short_description', models.TextField(max_length=100)),
                ('property_brief_description', models.TextField()),
                ('property_uploaded_by', models.CharField(max_length=50)),
                ('admin_name', models.CharField(max_length=50)),
                ('property_image', models.ImageField(upload_to='image/property')),
                ('keyword', models.CharField(max_length=50)),
                ('property_location', models.TextField()),
                ('property_city_address', models.CharField(max_length=50)),
                ('property_state_address', models.CharField(max_length=50)),
                ('property_country_address', models.CharField(max_length=50)),
                ('property_type', models.CharField(max_length=50)),
                ('property_status', models.CharField(max_length=50)),
                ('agent_name', models.CharField(max_length=50)),
                ('total_bedroom', models.IntegerField()),
                ('total_bathroom', models.IntegerField()),
                ('minimum_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maximum_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maximum_area', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
