# Generated by Django 2.1.11 on 2020-01-20 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0013_procedure_center_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endocenter',
            name='user_registered',
        ),
    ]
