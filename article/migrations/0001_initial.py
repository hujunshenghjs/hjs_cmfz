# Generated by Django 2.0.6 on 2020-04-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('guru_id', models.CharField(blank=True, max_length=11, null=True)),
                ('new_img', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img')),
            ],
            options={
                'db_table': 't_pic',
            },
        ),
    ]
