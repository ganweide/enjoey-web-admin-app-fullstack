# Generated by Django 4.2.7 on 2024-02-19 03:38

from django.db import migrations, models
import enjoey_api.storagebackend


class Migration(migrations.Migration):

    dependencies = [
        ('enjoey_api', '0023_alter_documentstable_documenturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentstable',
            name='documentURL',
            field=models.FileField(blank=True, null=True, storage=enjoey_api.storagebackend.DocumentsStorage(), upload_to=''),
        ),
    ]
