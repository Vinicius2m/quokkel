# Generated by Django 4.0.4 on 2022-05-26 16:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCategory',
            fields=[
                ('room_category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=150, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_guest_number', models.IntegerField()),
            ],
        ),
    ]
