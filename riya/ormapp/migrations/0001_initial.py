# Generated by Django 5.0.2 on 2024-02-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('author_name', models.CharField(max_length=50)),
                ('author_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
