# Generated by Django 2.1.4 on 2018-12-12 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.PositiveIntegerField()),
                ('user_id', models.PositiveIntegerField(blank=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('enquiry_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
