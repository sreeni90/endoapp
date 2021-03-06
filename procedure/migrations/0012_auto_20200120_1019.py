# Generated by Django 2.1.11 on 2020-01-20 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0011_endocenter_endoequipment_endominiclip_endopatient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endominiclip',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='miniclip', to='procedure.Procedure', unique=True),
        ),
    ]
