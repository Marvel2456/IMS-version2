# Generated by Django 3.2.8 on 2022-05-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0006_auto_20220503_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='debtor',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicaldebtor',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
    ]