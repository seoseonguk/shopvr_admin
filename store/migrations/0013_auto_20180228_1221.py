# Generated by Django 2.0.1 on 2018-02-28 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20180228_1023'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='naversearching',
            unique_together={('store', 'date')},
        ),
    ]
