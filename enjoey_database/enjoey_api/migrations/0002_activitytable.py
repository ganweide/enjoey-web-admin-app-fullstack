# Generated by Django 4.2.2 on 2023-06-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enjoey_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTable',
            fields=[
                ('activityId', models.CharField(db_index=True, max_length=250, primary_key=True, serialize=False)),
                ('activityType', models.CharField(max_length=250)),
                ('student', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('foodType', models.CharField(max_length=250)),
                ('foodQuantity', models.CharField(max_length=250)),
                ('mealType', models.CharField(max_length=250)),
                ('mealItem', models.CharField(max_length=250)),
                ('note', models.CharField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
            ],
        ),
    ]
