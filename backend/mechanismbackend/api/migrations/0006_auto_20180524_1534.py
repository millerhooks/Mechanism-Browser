# Generated by Django 2.0.4 on 2018-05-24 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180524_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanism',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='mechanism',
            name='name',
            field=models.CharField(default='Mechanism Request', max_length=200),
        ),
        migrations.AlterField(
            model_name='mechanism',
            name='transmission',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]