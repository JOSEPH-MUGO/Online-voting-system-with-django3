# Generated by Django 5.0.3 on 2024-03-11 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_alter_candidate_id_alter_position_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='bio',
        ),
    ]
