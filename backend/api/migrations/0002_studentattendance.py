# Generated by Django 5.1.1 on 2024-09-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('roll_number', models.CharField(max_length=50)),
                ('staff_name', models.CharField(max_length=255)),
                ('subject_code', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('location', models.JSONField()),
                ('code', models.CharField(max_length=50)),
            ],
        ),
    ]