# Generated by Django 2.2 on 2020-04-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='image/posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='image/posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='image/posts/'),
        ),
    ]