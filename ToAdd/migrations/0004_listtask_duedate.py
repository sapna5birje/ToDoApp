# Generated by Django 4.0.4 on 2022-05-08 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToAdd', '0003_alter_listtask_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='listtask',
            name='DueDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
