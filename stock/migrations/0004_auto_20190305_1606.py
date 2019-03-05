# Generated by Django 2.1.7 on 2019-03-05 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_release_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='office',
            name='slug',
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Separeted', 'Separeted'), ('Widow', 'Widow')], default='single', max_length=9),
        ),
        migrations.AlterField(
            model_name='customer',
            name='year',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th')], default='1st', max_length=9),
        ),
    ]
