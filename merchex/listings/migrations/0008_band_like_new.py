# Generated by Django 4.2.4 on 2023-08-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_listing_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_new',
            field=models.BooleanField(default=False),
        ),
    ]
