# Generated by Django 3.1.4 on 2020-12-17 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gvozdje', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gvozdje',
            name='mrezaZaKojuSeKoristi',
        ),
        migrations.AddField(
            model_name='mreza',
            name='odGvzdja',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gvozdje.gvozdje'),
            preserve_default=False,
        ),
    ]
