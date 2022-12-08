# Generated by Django 4.1.1 on 2022-12-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HungrezyApp', '0019_rider'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_account',
            fields=[
                ('bus_acc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('res_name', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=20)),
                ('food_type', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('contact_no', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]