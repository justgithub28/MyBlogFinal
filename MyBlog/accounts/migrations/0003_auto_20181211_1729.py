# Generated by Django 2.1.2 on 2018-12-11 11:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181211_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mob_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True),
        ),
    ]
