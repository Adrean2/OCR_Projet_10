# Generated by Django 4.0.1 on 2022-01-21 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='projects',
            new_name='project',
        ),
    ]