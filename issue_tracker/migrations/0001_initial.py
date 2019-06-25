# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-24 19:54
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
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('upvotes', models.IntegerField(default=0)),
                ('contibutions', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('ticket_type', models.CharField(choices=[('F', 'Feature'), ('B', 'Bug')], max_length=1)),
                ('status', models.CharField(choices=[('0', 'Completed'), ('1', 'In Progress'), ('2', 'On Hold'), ('5', 'Abandoned')], default='1', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]