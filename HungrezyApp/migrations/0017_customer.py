# Generated by Django 4.1.2 on 2022-12-06 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HungrezyApp', '0016_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.TextField()),
                ('contact_number', models.CharField(max_length=11)),
                ('gender', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]