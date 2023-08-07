# Generated by Django 3.2 on 2022-05-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_auto_20220519_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200, unique=True)),
                ('Phone', models.CharField(max_length=200, unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('Batch', models.CharField(max_length=200)),
                ('Pemail', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200, unique=True)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]
