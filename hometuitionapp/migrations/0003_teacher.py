# Generated by Django 3.1.1 on 2020-09-25 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hometuitionapp', '0002_auto_20200926_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('photo', models.ImageField(upload_to='teacher')),
                ('phone_no', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=40)),
                ('education', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=40)),
                ('cv', models.FileField(upload_to='cv')),
                ('citizenship', models.FileField(upload_to='citizenship')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hometuitionapp.course')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hometuitionapp.subject')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
