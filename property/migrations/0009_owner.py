# Generated by Django 2.2.4 on 2020-01-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200124_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца')),
                ('customer_phonenumber', models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца')),
                ('customer_phone_pure', models.CharField(blank=True, db_index=True, max_length=20, verbose_name='Нормализованый номер владельца')),
                ('customer_flat', models.ManyToManyField(related_name='flat_set', to='property.Flat', verbose_name='Квартиры в собствености:')),
            ],
        ),
    ]
