# Generated by Django 4.0.4 on 2022-04-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images'),
        ),
    ]