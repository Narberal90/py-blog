# Generated by Django 4.1 on 2024-09-13 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentary',
            options={'ordering': ['-created_time'], 'verbose_name_plural': 'comments'},
        ),
    ]
