# Generated by Django 3.2.5 on 2021-11-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_order_table_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg_donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Place', models.CharField(max_length=200)),
                ('Phone', models.CharField(max_length=200)),
                ('Bgroup', models.CharField(max_length=200)),
                ('Aadhar', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200, unique=True)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]