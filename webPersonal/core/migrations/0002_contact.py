# Generated by Django 4.0.3 on 2022-05-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150, verbose_name='Asunto')),
                ('message', models.CharField(max_length=400, verbose_name='Mensaje')),
            ],
        ),
    ]
