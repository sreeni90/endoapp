# Generated by Django 2.1.11 on 2020-01-20 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0005_auto_20200120_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endopolyp',
            name='procedure_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Procedure_Polyp', to='procedure.Procedure'),
        ),
    ]
