# Generated by Django 2.1.5 on 2019-03-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField()),
                ('about_image', models.ImageField(upload_to='image/about')),
                ('video', models.FileField(upload_to='video/about')),
            ],
        ),
    ]
