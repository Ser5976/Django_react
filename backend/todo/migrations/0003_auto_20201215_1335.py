# Generated by Django 3.1.3 on 2020-12-15 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201215_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('country', models.CharField(max_length=50, verbose_name='Address')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('street', models.CharField(max_length=50, verbose_name='Street')),
                ('house', models.CharField(max_length=25, verbose_name='Street')),
                ('zip_code', models.IntegerField(verbose_name='Zip code')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.address'),
        ),
    ]
