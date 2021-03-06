# Generated by Django 4.0.2 on 2022-02-25 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('pub_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'db_article',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('regdate', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'db_guest',
            },
        ),
    ]
