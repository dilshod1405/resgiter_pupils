# Generated by Django 4.0.6 on 2022-08-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Region',
            },
        ),
        migrations.CreateModel(
            name='School_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'school location',
            },
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('class_number', models.IntegerField(max_length=2)),
                ('birth_date', models.DateField()),
                ('birth_address', models.ManyToManyField(to='registration.region')),
                ('studying_address', models.ManyToManyField(to='registration.school_location')),
            ],
            options={
                'db_table': 'Pupil',
            },
        ),
    ]
