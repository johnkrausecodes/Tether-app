# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-08 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tether', '0091_remove_userprofile1_recent_matches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles_matches',
            name='match_id',
        ),
        migrations.RemoveField(
            model_name='profiles_matches',
            name='profile_id',
        ),
        migrations.DeleteModel(
            name='Profiles_Matches',
        ),
    ]