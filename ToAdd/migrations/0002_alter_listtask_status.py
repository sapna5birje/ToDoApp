# Generated by Django 4.0.4 on 2022-05-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToAdd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listtask',
            name='Status',
            field=models.IntegerField(choices=[(1, 'Started'), (2, 'Inprogress'), (3, 'Completed')], default=1),
        ),
    ]