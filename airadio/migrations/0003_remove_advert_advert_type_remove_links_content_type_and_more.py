# Generated by Django 4.2.8 on 2024-01-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airadio', '0002_remove_dashboardtopsongs_twitter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='advert_type',
        ),
        migrations.RemoveField(
            model_name='links',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='links',
            name='link_type',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='skipped',
        ),
        migrations.AlterField(
            model_name='advert',
            name='skip_allowed',
            field=models.BooleanField(default=True, verbose_name='Skip allowed'),
        ),
        migrations.AlterField(
            model_name='adverts',
            name='type',
            field=models.CharField(blank=True, choices=[('audio', 'Audio'), ('video', 'Video')], max_length=255, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='wall',
            name='media_type',
            field=models.CharField(blank=True, choices=[('audio', 'Audio'), ('video', 'Video')], max_length=200, null=True, verbose_name='Media Type'),
        ),
    ]