# Generated by Django 5.0.1 on 2024-02-20 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_reseña'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reseña',
            old_name='opinion',
            new_name='reseña',
        ),
        migrations.RemoveField(
            model_name='reseña',
            name='apellido',
        ),
    ]
