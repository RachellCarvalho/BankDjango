# Generated by Django 2.2.5 on 2021-07-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bankapp', '0009_alter_transaction_tdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]