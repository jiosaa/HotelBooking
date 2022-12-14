# Generated by Django 4.0.6 on 2022-08-19 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_finishpayment_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Hotel.paymentinformations'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.hotel'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hotel.roomgroup'),
        ),
    ]
