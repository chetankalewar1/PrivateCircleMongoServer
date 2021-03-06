# Generated by Django 4.0.3 on 2022-03-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquityStockWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=255)),
                ('open', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ltp', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change', models.DecimalField(decimal_places=2, max_digits=10)),
                ('change_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('turnover', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_52', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_52', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chang_percent_365', models.DecimalField(decimal_places=2, max_digits=10)),
                ('chang_percent_30', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
