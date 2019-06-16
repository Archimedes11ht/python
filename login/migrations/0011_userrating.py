# Generated by Django 2.1.1 on 2019-06-11 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_delete_movies_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=128, unique=True)),
                ('user_span', models.CharField(max_length=50)),
                ('movie_title', models.CharField(max_length=128)),
                ('user_comment', models.CharField(max_length=400)),
            ],
        ),
    ]