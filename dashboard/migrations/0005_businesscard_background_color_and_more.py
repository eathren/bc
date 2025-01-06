# Generated by Django 5.1.4 on 2025-01-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_businesscard_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscard',
            name='background_color',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AddField(
            model_name='businesscard',
            name='icon_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='businesscard',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='businesscard',
            name='theme',
            field=models.CharField(default='default', max_length=50),
        ),
    ]