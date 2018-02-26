# Generated by Django 2.0.1 on 2018-02-25 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20180225_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_cash_sales', models.IntegerField()),
                ('pos_card_sales', models.IntegerField()),
                ('kiosk_cash_sales', models.IntegerField()),
                ('kiosk_cash_saels', models.IntegerField()),
                ('total_sales', models.IntegerField()),
                ('date', models.DateField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
    ]
