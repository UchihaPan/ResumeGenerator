# Generated by Django 3.1.3 on 2020-11-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20201108_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='photo',
            field=models.ImageField(default='user.jpg', upload_to='profiles/'),
        ),
    ]
