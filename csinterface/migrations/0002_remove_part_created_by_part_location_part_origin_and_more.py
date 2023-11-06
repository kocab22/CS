# Generated by Django 4.2.2 on 2023-08-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csinterface', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='created_by',
        ),
        migrations.AddField(
            model_name='part',
            name='location',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='origin',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='part',
            name='picked_up',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='part',
            name='request',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='reservation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='status',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='part',
            name='stock_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='part',
            name='supplier',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='part',
            name='description',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='part',
            name='number',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
