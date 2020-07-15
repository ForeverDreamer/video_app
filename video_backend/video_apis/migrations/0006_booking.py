# Generated by Django 2.2 on 2019-07-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_apis', '0005_auto_20190719_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('placeId', models.CharField(max_length=50)),
                ('placeTitle', models.CharField(max_length=50)),
                ('placeImage', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('guestNumber', models.IntegerField()),
                ('bookedFrom', models.DateTimeField()),
                ('bookedTo', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
