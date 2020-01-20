# Generated by Django 2.1.11 on 2020-01-20 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0008_remove_procedure_polyp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endopolyp',
            name='procedure_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polyp', to='procedure.Procedure'),
        ),
    ]
