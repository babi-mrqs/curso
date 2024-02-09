# Generated by Django 4.2.6 on 2023-11-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_todo_deadline_alter_todo_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(verbose_name='Prazo'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
