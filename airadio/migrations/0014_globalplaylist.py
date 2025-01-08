# Generated by Django 4.2.8 on 2024-05-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airadio', '0013_alter_adverts_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'News'), (2, 'Weather'), (4, 'Entertainment'), (5, 'Sports')], default=1, verbose_name='Type')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('media', models.URLField(verbose_name='Media URL')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Global Playlist',
                'verbose_name_plural': 'Global Playlists',
                'ordering': ['-id'],
            },
        ),
    ]
