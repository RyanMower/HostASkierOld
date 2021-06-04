# Generated by Django 3.2.3 on 2021-06-03 23:09

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
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default='0', max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default='0', max_digits=9)),
                ('price', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('boat_type', models.CharField(max_length=100)),
                ('events_can_pull', models.CharField(max_length=100)),
                ('hostest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]