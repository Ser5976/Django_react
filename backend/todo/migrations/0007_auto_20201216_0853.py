# Generated by Django 3.1.3 on 2020-12-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20201216_0840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='house',
            new_name='item',
        ),
        migrations.AddField(
            model_name='address',
            name='house_number',
            field=models.CharField(default=12, max_length=25, verbose_name='Street'),
            preserve_default=False,
        ),
    ]
