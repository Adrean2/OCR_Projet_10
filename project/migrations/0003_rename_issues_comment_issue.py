# Generated by Django 4.0.1 on 2022-01-21 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_rename_projects_issue_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='issues',
            new_name='issue',
        ),
    ]
