# Generated by Django 2.1.11 on 2020-01-17 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EndoPolyp',
            fields=[
                ('polyp_id', models.AutoField(primary_key=True, serialize=False)),
                ('procedure_id', models.IntegerField()),
                ('size', models.IntegerField()),
                ('removed_flag', models.BooleanField()),
                ('removed_by_equipment', models.BooleanField()),
                ('location', models.CharField(max_length=500)),
                ('morphology', models.CharField(max_length=100)),
                ('scope_length_marker', models.IntegerField()),
                ('pathalogy_indicator', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Polyp',
                'db_table': 'endo_polyp',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedure_id', models.CharField(max_length=255, null=True, verbose_name='Procedure Id')),
                ('room_id', models.IntegerField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('cecum_time', models.DateTimeField(null=True)),
                ('inside_time', models.DateTimeField(null=True)),
                ('stop_time', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Procedure',
                'verbose_name_plural': 'Procedures',
                'db_table': 'endo_procedure',
                'managed': True,
            },
        ),
    ]
