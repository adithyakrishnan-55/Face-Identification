# Generated by Django 3.2 on 2022-05-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usernm', models.CharField(max_length=200)),
                ('Date', models.CharField(max_length=200)),
                ('Punchin', models.CharField(max_length=200)),
                ('Punchout', models.CharField(default='0', max_length=200)),
            ],
        ),
    ]
