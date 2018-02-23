# Generated by Django 2.0.1 on 2018-02-15 04:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('store', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
