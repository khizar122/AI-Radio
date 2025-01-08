# Generated by Django 4.2.8 on 2024-08-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airadio", "0014_globalplaylist"),
    ]

    operations = [
        migrations.AddField(
            model_name="library",
            name="lyrics",
            field=models.URLField(blank=True, null=True, verbose_name="Lyrics URL"),
        ),
    ]