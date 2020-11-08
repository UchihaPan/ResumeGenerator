# Generated by Django 3.1.3 on 2020-11-08 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20201108_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='github',
            field=models.URLField(blank=True, default='https://github.com/', max_length=255),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='linkedin',
            field=models.URLField(blank=True, default='https://www.linkedin.com/feed/', max_length=255),
        ),
    ]