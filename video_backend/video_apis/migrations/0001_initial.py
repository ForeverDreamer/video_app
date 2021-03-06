# Generated by Django 2.2 on 2019-07-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image_url', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
            ],
        ),
    ]
