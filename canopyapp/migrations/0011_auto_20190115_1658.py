# Generated by Django 2.1 on 2019-01-15 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canopyapp', '0010_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
