# Generated by Django 3.1.3 on 2020-11-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.TextField()),
                ('age', models.IntegerField()),
                ('money', models.IntegerField()),
                ('max_health', models.IntegerField(null=True)),
                ('friends_alive', models.IntegerField(null=True)),
            ],
        ),
    ]
