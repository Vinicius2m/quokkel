# Generated by Django 4.0.4 on 2022-05-26 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0001_initial'),
        ('rooms', '0001_initial'),
        ('room_categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='rooms.room'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room_categories.roomcategory'),
        ),
    ]
