# Generated by Django 2.1.8 on 2019-09-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='cpostcode',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='client',
            name='cstate',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='cstreet',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='csuburb',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
