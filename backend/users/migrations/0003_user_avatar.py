# Generated by Django 3.1.3 on 2021-01-09 15:24

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='', upload_to=users.models.avatar_path, verbose_name='Avatar'),
        ),
    ]
