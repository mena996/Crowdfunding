# Generated by Django 2.1 on 2020-04-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20200424_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='body',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4)),
        ),
    ]
