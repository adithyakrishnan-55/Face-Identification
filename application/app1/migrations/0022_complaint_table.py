# Generated by Django 3.2 on 2022-02-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_leave_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usernm', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Complaint', models.CharField(max_length=200)),
            ],
        ),
    ]
