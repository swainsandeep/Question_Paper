# Generated by Django 2.1rc1 on 2020-06-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='routerdeails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.CharField(max_length=18)),
                ('hostname', models.CharField(max_length=14)),
                ('loopback', models.CharField(max_length=14)),
                ('macadress', models.CharField(max_length=17)),
            ],
        ),
    ]