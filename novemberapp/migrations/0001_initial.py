# Generated by Django 5.1.3 on 2024-11-19 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('cnumber', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
