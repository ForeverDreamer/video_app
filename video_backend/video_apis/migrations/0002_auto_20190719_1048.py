# Generated by Django 2.2 on 2019-07-19 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='date_from',
            new_name='availableFrom',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='date_to',
            new_name='availableTo',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='image_url',
            new_name='imageUrl',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='user_id',
            new_name='userId',
        ),
    ]
