# Generated by Django 2.0.1 on 2018-02-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highTemp', models.CharField(max_length=140)),
                ('lowTemp', models.CharField(max_length=140)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
