# Generated by Django 3.1.4 on 2020-12-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hometuitionapp', '0002_auto_20201220_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hometuitionsystem',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
