# Generated by Django 2.0.7 on 2018-07-29 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
