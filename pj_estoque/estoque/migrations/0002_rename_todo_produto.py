# Generated by Django 4.2.7 on 2023-11-14 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Produto',
        ),
    ]
