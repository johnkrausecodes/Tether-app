# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-08 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tether', '0092_auto_20170308_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles_Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.NewRecentMatches1')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tether.UserProfile1')),
            ],
            options={
                'db_table': 'profiles_matches',
                'verbose_name_plural': 'Recent matches',
            },
        ),
        migrations.AddField(
            model_name='userprofile1',
            name='recent_matches',
            field=models.ManyToManyField(through='tether.Profiles_Matches', to='tether.NewRecentMatches1'),
        ),
    ]