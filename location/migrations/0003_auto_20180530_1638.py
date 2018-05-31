# Generated by Django 2.0.1 on 2018-05-30 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20180515_1236'),
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
        migrations.CreateModel(
            name='MarketingArea',
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
                ('title', models.CharField(max_length=20)),
                ('location_class', models.CharField(choices=[('UV', '대학'), ('OF', '오피스'), ('LV', '주거'), ('TF', '교통')], max_length=20)),
                ('comsumption_propensity', models.CharField(choices=[('ENTERTAINMENT', '유흥'), ('SHOPPING', '쇼핑'), ('OVERALL', '종합'), ('DATING', '데이트')], max_length=20)),
                ('location_point', models.IntegerField()),
                ('location_grade', models.CharField(choices=[('B', 'B'), ('C', 'C'), ('A', 'A'), ('S', 'S')], max_length=20)),
                ('escape_room', models.IntegerField()),
                ('animal_cafe', models.IntegerField()),
                ('healing_cafe', models.IntegerField()),
                ('comic_book_cafe', models.IntegerField()),
                ('arrow_cafe', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MarketingAreaTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubwayStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('distance_one', models.ManyToManyField(related_name='univ_distance_one', to='location.SubwayStation')),
                ('distance_two', models.ManyToManyField(related_name='univ_distance_two', to='location.SubwayStation')),
                ('distance_zero', models.ManyToManyField(related_name='univ_distance_zero', to='location.SubwayStation')),
                ('distnace_three', models.ManyToManyField(related_name='univ_distance_three', to='location.SubwayStation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='LocationTag',
        ),
        migrations.RemoveField(
            model_name='location',
            name='escape_room',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_class',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_grade',
        ),
        migrations.RemoveField(
            model_name='location',
            name='x_axis',
        ),
        migrations.RemoveField(
            model_name='location',
            name='y_axis',
        ),
        migrations.AddField(
            model_name='location',
            name='additional_address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='location',
            name='contact_info',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='deposit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='level',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='lnglat',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='maintainence_cost',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='monthly_rent_fee',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='premium_deposit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marketingarea',
            name='subway_station',
            field=models.ManyToManyField(to='location.SubwayStation'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='marketing_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.MarketingArea'),
        ),
    ]