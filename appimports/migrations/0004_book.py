# Generated by Django 4.0.4 on 2022-05-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appimports', '0003_remove_salesdata_address_line1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Book name')),
                ('author_email', models.EmailField(blank=True, max_length=75, verbose_name='Author email')),
                ('imported', models.BooleanField(default=False)),
                ('published', models.DateField(blank=True, null=True, verbose_name='Published')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
