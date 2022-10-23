# Generated by Django 4.1.1 on 2022-10-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HungrezyApp', '0006_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_made_food',
            fields=[
                ('hmf_suppiler_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('o_id', models.IntegerField(primary_key=True, serialize=False)),
                ('number_of_servings', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]