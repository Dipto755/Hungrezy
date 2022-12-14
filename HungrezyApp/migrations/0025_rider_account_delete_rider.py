# Generated by Django 4.1.1 on 2022-12-08 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HungrezyApp', '0024_rename_name_rider_u_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='rider_account',
            fields=[
                ('rid_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.TextField()),
                ('delivary_method', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('contact_number', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='rider',
        ),
    ]
