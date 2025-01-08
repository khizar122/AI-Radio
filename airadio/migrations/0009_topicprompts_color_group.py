# Generated by Django 4.2.8 on 2024-02-05 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airadio', '0008_positionprompts_topicprompts'),
    ]

    operations = [
        migrations.AddField(
            model_name='topicprompts',
            name='color_group',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Green'), (2, 'Blue'), (3, 'Red'), (4, 'Yellow')], default=1),
            preserve_default=False,
        ),
    ]
