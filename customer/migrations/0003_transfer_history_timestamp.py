# Generated by Django 3.0.5 on 2021-04-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_transfer_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer_history',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
