# Generated by Django 3.2 on 2022-02-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_complaint_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usernm', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Month', models.CharField(max_length=200)),
                ('Total_attendance', models.CharField(max_length=200)),
                ('Worked_hours', models.CharField(max_length=200)),
                ('Salary', models.CharField(max_length=200)),
            ],
        ),
    ]
