# Generated by Django 2.0.1 on 2018-04-21 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_naversearching_is_mobile'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='naversearching',
            unique_together={('store', 'date', 'keyword', 'is_mobile')},
        ),
    ]