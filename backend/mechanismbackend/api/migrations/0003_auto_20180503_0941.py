# Generated by Django 2.0.4 on 2018-05-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180426_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanism',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
