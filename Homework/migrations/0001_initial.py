# Generated by Django 3.1.7 on 2021-03-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title_homework', models.CharField(max_length=50)),
                ('student_number', models.CharField(max_length=50)),
                ('last_post_time', models.DateTimeField(auto_now=True)),
                ('File', models.FileField(upload_to='AnswerFolder')),
                ('score', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('HWFile', models.FileField(upload_to='HomeWorkFolder')),
            ],
        ),
    ]
