# Generated by Django 2.2.6 on 2019-10-29 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='B1io',
            new_name='Bio',
        ),
    ]