# Generated by Django 2.1.2 on 2018-12-12 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_email_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mob_no',
        ),
    ]