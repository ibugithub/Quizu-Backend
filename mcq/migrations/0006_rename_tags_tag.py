# Generated by Django 5.0.3 on 2024-04-27 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0005_question_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
