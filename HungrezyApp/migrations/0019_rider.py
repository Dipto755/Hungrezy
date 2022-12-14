# Generated by Django 4.1.1 on 2022-12-07 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HungrezyApp', '0018_delete_rider'),
    ]

    operations = [
        migrations.CreateModel(
            name='rider',
            fields=[
                ('rid_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.TextField()),
                ('delivary_method', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
