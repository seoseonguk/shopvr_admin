# Generated by Django 2.0.1 on 2018-02-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180223_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='slug',
            field=models.CharField(default='hd1', max_length=10),
            preserve_default=False,
        ),
    ]