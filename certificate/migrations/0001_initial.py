# Generated by Django 4.0.1 on 2022-01-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=55)),
                ('student_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact_number', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('total_attendance', models.IntegerField(default=0)),
                ('reference_number', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
