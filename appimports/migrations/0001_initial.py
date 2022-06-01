# Generated by Django 4.0.4 on 2022-05-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price_each', models.IntegerField()),
                ('orderlinenum', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('orderdate', models.DateField()),
                ('status', models.CharField(max_length=12)),
                ('qtr_id', models.IntegerField()),
                ('month_id', models.IntegerField()),
                ('year_id', models.IntegerField()),
                ('product_line', models.CharField(max_length=40)),
                ('msrp', models.IntegerField()),
                ('product_code', models.IntegerField()),
                ('customer_name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('address_line1', models.CharField(max_length=50)),
                ('address_line2', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('territory', models.CharField(max_length=30)),
                ('contactlastname', models.CharField(max_length=40)),
                ('contactfirstname', models.CharField(max_length=40)),
                ('dealsize', models.CharField(max_length=18)),
            ],
        ),
    ]