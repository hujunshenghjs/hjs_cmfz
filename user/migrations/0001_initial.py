# Generated by Django 2.0.6 on 2020-04-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
                ('head_pic', models.ImageField(upload_to='head_picture')),
                ('user_info', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('salt', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
