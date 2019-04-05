# Generated by Django 2.2 on 2019-04-02 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=25)),
                ('artist_name', models.CharField(max_length=30)),
                ('album_genre', models.CharField(max_length=10)),
                ('album_cover', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=25)),
                ('song_audio', models.FileField(upload_to='')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trap.Album')),
            ],
        ),
    ]
