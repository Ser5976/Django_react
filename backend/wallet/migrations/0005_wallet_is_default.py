# Generated by Django 3.1.3 on 2021-02-18 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20210123_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Is default'),
        ),
    ]
