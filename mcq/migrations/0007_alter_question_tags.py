# Generated by Django 5.0.3 on 2024-04-27 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0006_rename_tags_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='mcq.tag'),
        ),
    ]