# Generated by Django 2.1.5 on 2019-03-16 18:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('Catagory_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Catagory_name', models.CharField(max_length=30)),
                ('Is_Valid', models.CharField(default='active', max_length=20)),
                ('Created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('Modified_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
