# Generated by Django 4.1.3 on 2022-12-06 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plannerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tripRecm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('month', models.DateField()),
                ('dest', models.TextField()),
                ('num', models.IntegerField()),
                ('descp', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='tripInfo',
        ),
    ]