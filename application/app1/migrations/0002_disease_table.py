# Generated by Django 3.2.5 on 2021-11-08 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dname', models.CharField(max_length=200)),
                ('Symptoms', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
