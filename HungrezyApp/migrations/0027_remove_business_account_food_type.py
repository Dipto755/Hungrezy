# Generated by Django 4.1.2 on 2022-12-09 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HungrezyApp', '0026_customer_account_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business_account',
            name='food_type',
        ),
    ]