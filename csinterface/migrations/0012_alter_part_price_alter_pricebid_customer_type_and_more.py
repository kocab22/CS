# Generated by Django 4.2.2 on 2023-10-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csinterface', '0011_pricebid_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricebid',
            name='customer_type',
            field=models.CharField(choices=[('RG', 'Regular'), ('DL', 'Dealer'), ('GR', 'Tajmac Group')], default='RG', max_length=2),
        ),
        migrations.AlterField(
            model_name='pricebid',
            name='text',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]