# Generated by Django 5.0.3 on 2024-04-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0007_alter_question_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tags', models.ManyToManyField(related_name='noteTags', to='mcq.tag')),
            ],
        ),
    ]
