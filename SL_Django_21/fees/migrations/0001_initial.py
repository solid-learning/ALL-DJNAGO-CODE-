# Generated by Django 3.2 on 2021-06-10 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=33)),
                ('stucollage', models.CharField(max_length=33)),
                ('stustate', models.CharField(max_length=33)),
                ('stupass', models.CharField(max_length=33)),
            ],
        ),
    ]
