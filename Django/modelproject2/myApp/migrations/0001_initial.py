# Generated by Django 4.0.3 on 2022-04-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('edesig', models.CharField(max_length=30)),
                ('edob', models.DateField()),
                ('eexp', models.FloatField()),
                ('esal', models.IntegerField()),
            ],
        ),
    ]
