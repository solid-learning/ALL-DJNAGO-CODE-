# Generated by Django 3.2 on 2021-06-13 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0002_auto_20210613_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='mail',
        ),
    ]
