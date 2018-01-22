# Generated by Django 2.0.1 on 2018-01-22 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]