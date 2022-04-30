# Generated by Django 3.2.8 on 2022-04-28 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('batch_no', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('Available', 'Item is currently available'), ('Restocking', 'Currently out of stock')], default='Available', max_length=20, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('mode_of_sales', models.CharField(blank=True, choices=[('General', 'General'), ('Promo', 'Promo')], default='General', max_length=50, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, default=0, null=True)),
                ('total_price', models.IntegerField(blank=True, default=0, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity_restocked', models.IntegerField(blank=True, default=0, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('store', models.IntegerField(blank=True, default=0, null=True)),
                ('variance', models.IntegerField(blank=True, default=0, null=True)),
                ('available', models.IntegerField(blank=True, default=0, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('batch_no', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default=10)),
                ('status', models.CharField(blank=True, choices=[('Available', 'Item is currently available'), ('Restocking', 'Currently out of stock')], default='Available', max_length=20, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('mode_of_sales', models.CharField(blank=True, choices=[('General', 'General'), ('Promo', 'Promo')], default='General', max_length=50, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, default=0, null=True)),
                ('total_price', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity_restocked', models.IntegerField(blank=True, default=0, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('store', models.IntegerField(default=0)),
                ('variance', models.IntegerField(default=0)),
                ('available', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ims.category')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalProductReport',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('batch_no', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('Available', 'Item is currently available'), ('Restocking', 'Currently out of stock')], default='Available', max_length=20, null=True)),
                ('last_updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('mode_of_sales', models.CharField(blank=True, choices=[('General', 'General'), ('Promo', 'Promo')], default='General', max_length=50, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, default=0, null=True)),
                ('total_price', models.IntegerField(blank=True, default=0, null=True)),
                ('amount', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity_restocked', models.IntegerField(blank=True, default=0, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('store', models.IntegerField(blank=True, default=0, null=True)),
                ('variance', models.IntegerField(blank=True, default=0, null=True)),
                ('available', models.IntegerField(blank=True, default=0, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('brand', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ims.brand')),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ims.category')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical product report',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('batch_no', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default=10)),
                ('status', models.CharField(blank=True, choices=[('Available', 'Item is currently available'), ('Restocking', 'Currently out of stock')], default='Available', max_length=20, null=True)),
                ('last_updated', models.DateTimeField(blank=True, editable=False)),
                ('timestamp', models.DateTimeField(blank=True, editable=False)),
                ('mode_of_sales', models.CharField(blank=True, choices=[('General', 'General'), ('Promo', 'Promo')], default='General', max_length=50, null=True)),
                ('quantity_sold', models.IntegerField(blank=True, default=0, null=True)),
                ('total_price', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity_restocked', models.IntegerField(blank=True, default=0, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('store', models.IntegerField(default=0)),
                ('variance', models.IntegerField(default=0)),
                ('available', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('brand', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ims.brand')),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ims.category')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
