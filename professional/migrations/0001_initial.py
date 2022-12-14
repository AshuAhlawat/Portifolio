# Generated by Django 4.1 on 2022-09-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('score', models.FloatField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer', models.CharField(max_length=50)),
                ('proof', models.ImageField(upload_to='')),
                ('employed', models.BooleanField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('job_title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('location', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(choices=[('Language', 'Language'), ('Framework', 'Framework'), ('Tools', 'Tools'), ('DataBase', 'Database'), ('Soft Skills', 'Soft Skills')], max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
