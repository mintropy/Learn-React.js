# Generated by Django 5.0.1 on 2024-11-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
