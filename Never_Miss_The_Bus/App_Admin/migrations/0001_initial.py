# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 11:04
from __future__ import unicode_literals

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
            name='Bus',
            fields=[
                ('bus_id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=30, verbose_name='Bus Name')),
                ('status', models.CharField(choices=[('REG', 'Registered'), ('OPN', 'Open/Not Registered')], default='OPN', max_length=3, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Buses',
            },
        ),
        migrations.CreateModel(
            name='Coord_Reporter',
            fields=[
                ('reporter_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('acceptance_date', models.DateTimeField(auto_now_add=True)),
                ('accepted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted_by', to=settings.AUTH_USER_MODEL)),
                ('allocated_bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Admin.Bus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reporter')),
            ],
            options={
                'verbose_name': 'Coordinates Reporters',
            },
        ),
        migrations.CreateModel(
            name='Coord_Reporter_Request',
            fields=[
                ('request_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('request_created_date_time', models.DateTimeField(auto_now_add=True, verbose_name='Request created on')),
                ('respond_date_time', models.DateTimeField(null=True)),
                ('respond_status', models.CharField(choices=[('NVR', 'Not Verified'), ('DND', 'Denied')], default='NVR', max_length=3)),
                ('requestedfor_bus_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Admin.Bus', verbose_name='Requesting for bus')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Requested by')),
            ],
            options={
                'verbose_name': 'Coordinates Reporting Requests',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Route ID')),
                ('route_name', models.CharField(max_length=50, unique=True, verbose_name='Route Name')),
            ],
            options={
                'verbose_name': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='Stop ID')),
                ('stop_name', models.CharField(max_length=50, unique=True, verbose_name='Stop Name')),
            ],
            options={
                'verbose_name': 'Stops',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_admin_origin_stop_related', to='App_Admin.Stop', verbose_name='Origin Stop'),
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(to='App_Admin.Stop', verbose_name='Stops'),
        ),
        migrations.AddField(
            model_name='bus',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Admin.Route', verbose_name='Route Number'),
        ),
    ]
