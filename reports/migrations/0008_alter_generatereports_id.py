# Generated by Django 3.2.3 on 2021-05-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20210513_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generatereports',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
