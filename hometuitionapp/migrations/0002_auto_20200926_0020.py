# Generated by Django 3.1.1 on 2020-09-25 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometuitionapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='course',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]