# Generated by Django 4.2.7 on 2023-11-14 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Título')),
                ('descricao', models.TextField(blank=True)),
                ('quantidade', models.PositiveIntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_att', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]