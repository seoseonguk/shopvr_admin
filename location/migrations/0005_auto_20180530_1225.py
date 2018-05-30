# Generated by Django 2.0.1 on 2018-05-30 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0004_auto_20180530_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.TextField(blank=True)),
                ('lnglat', models.CharField(max_length=50)),
                ('provinence', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('district_county_town', models.CharField(blank=True, max_length=10)),
                ('neighborhood_township_village', models.CharField(max_length=10)),
                ('additional_address', models.CharField(blank=True, max_length=100)),
                ('level', models.IntegerField(blank=True)),
                ('category', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('open_date', models.DateField(blank=True)),
                ('fee_for_couple', models.PositiveIntegerField()),
                ('operating_time_weekday', models.CharField(max_length=100)),
                ('operating_time_weekend', models.CharField(max_length=100)),
                ('is_steam_based', models.BooleanField()),
                ('is_drink_essential', models.BooleanField()),
                ('is_atraction_operating', models.CharField(max_length=100)),
                ('grade', models.IntegerField()),
                ('blog_link', models.URLField(max_length=100)),
                ('etc', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='location',
            name='x_axis',
        ),
        migrations.RemoveField(
            model_name='location',
            name='y_axis',
        ),
        migrations.RemoveField(
            model_name='marketingarea',
            name='x_axis',
        ),
        migrations.RemoveField(
            model_name='marketingarea',
            name='y_axis',
        ),
        migrations.AddField(
            model_name='location',
            name='lnglat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marketingarea',
            name='lnglat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competitor',
            name='marketing_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.MarketingArea'),
        ),
    ]