# Generated by Django 4.0.1 on 2022-01-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_contributor_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=models.CharField(choices=[('AUTHOR', 'Author'), ('PARTICIPANT', 'Participant')], default='PARTICIPANT', max_length=11),
        ),
    ]
