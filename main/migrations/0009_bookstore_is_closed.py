# Generated by Django 3.1.3 on 2021-01-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_bookstore_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
