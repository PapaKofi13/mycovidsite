# Generated by Django 2.1.7 on 2020-05-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchUserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='email ')),
                ('mobile_num', models.IntegerField(verbose_name='Phone Number')),
                ('level', models.IntegerField(verbose_name='Level')),
                ('course', models.CharField(max_length=50, verbose_name='Course')),
                ('date_posted', models.DateTimeField(auto_now=True, verbose_name='Date')),
            ],
        ),
    ]
