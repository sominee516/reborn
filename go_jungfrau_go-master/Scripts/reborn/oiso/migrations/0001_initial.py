# Generated by Django 3.1.3 on 2021-12-06 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apt_geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apt_code', models.CharField(max_length=20)),
                ('apt_latest', models.CharField(max_length=100)),
                ('apt_lat', models.CharField(max_length=50)),
                ('apt_lng', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='apt_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apt_code', models.CharField(max_length=20)),
                ('apt_name', models.CharField(max_length=100)),
                ('apt_juso', models.CharField(max_length=300)),
                ('apt_since', models.CharField(max_length=50)),
                ('apt_pop', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='apt_sil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apt_code', models.CharField(max_length=20)),
                ('apt_name', models.CharField(max_length=100)),
                ('apt_year', models.CharField(max_length=20)),
                ('apt_price', models.CharField(max_length=50)),
            ],
        ),
    ]