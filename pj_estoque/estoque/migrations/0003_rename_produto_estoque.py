# Generated by Django 4.2.7 on 2023-11-16 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_rename_todo_produto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produto',
            new_name='Estoque',
        ),
    ]
