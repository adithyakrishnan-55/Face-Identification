# Generated by Django 3.2 on 2022-05-19 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_remove_salary_table_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reg_employee',
            new_name='Reg_student',
        ),
        migrations.DeleteModel(
            name='Attendance_table',
        ),
        migrations.DeleteModel(
            name='Complaint_table',
        ),
        migrations.DeleteModel(
            name='Leave_table',
        ),
        migrations.DeleteModel(
            name='Salary_table',
        ),
    ]