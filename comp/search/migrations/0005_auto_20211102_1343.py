# Generated by Django 3.2.8 on 2021-11-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20211102_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='phone',
            name='link',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]