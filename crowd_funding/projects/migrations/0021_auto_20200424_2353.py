# Generated by Django 2.1 on 2020-04-24 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_merge_20200424_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='body',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4)),
        ),
    ]