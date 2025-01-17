# Generated by Django 5.0.7 on 2024-08-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=100, verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='source',
            field=models.CharField(max_length=100, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.PositiveIntegerField(max_length=6),
        ),
    ]
