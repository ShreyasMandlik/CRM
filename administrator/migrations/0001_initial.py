# Generated by Django 4.0.1 on 2022-02-08 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Service_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Sales_count', models.IntegerField(blank=True, null=True)),
                ('Charges', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('Sales_count', models.IntegerField(blank=True, null=True)),
                ('Client_count', models.IntegerField(blank=True, null=True)),
                ('Agent_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Agent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
