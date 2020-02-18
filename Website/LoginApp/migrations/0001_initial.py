# Generated by Django 2.2.5 on 2020-01-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpModel',
            fields=[
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
    ]
