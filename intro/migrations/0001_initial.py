# Generated by Django 4.1 on 2022-09-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Ashwani Ahlawat', max_length=20)),
                ('position', models.CharField(default='Instructor', max_length=25)),
                ('dp', models.ImageField(default='images/dp.jpeg', upload_to='images')),
                ('zipcode', models.IntegerField(default=100000)),
                ('address', models.TextField(default='India, Haryana')),
                ('phone', models.CharField(default='+91-9876543210', max_length=15)),
                ('email', models.EmailField(default='ashwaniahlawat22@gmail.com', max_length=254)),
                ('github', models.URLField(default='https://github.com/AshuAhlawat')),
                ('linkdin', models.URLField(default='https://www.linkedin.com/in/ashwani-ahlawat/')),
                ('other', models.URLField(default='https://myanimelist.net/animelist/Capti')),
            ],
        ),
    ]
