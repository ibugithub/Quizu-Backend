# Generated by Django 5.0.3 on 2024-04-27 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0004_tags_alter_question_quiz_alter_quiz_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='mcq.tags'),
        ),
    ]
