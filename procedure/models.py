from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Procedure(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    procedure_id = models.CharField(_("Procedure Id"), max_length=255,null=True)
    center = models.ForeignKey('EndoCenter',related_name='center',on_delete=models.SET_DEFAULT,null=True,default=None)
    room_id = models.IntegerField(null=True)
    start_time = models.DateTimeField(null=True)
    cecum_time = models.DateTimeField(null=True)
    inside_time = models.DateTimeField(null=True)
    stop_time = models.DateTimeField(null=True)
    class Meta:
        managed = True
        app_label = 'procedure'
        db_table = 'endo_procedure'
        verbose_name = _("Procedure")
        verbose_name_plural = _("Procedures")

    def __str__(self):
        return smart_unicode(self.procedure_id)

    def __unicode__(self):
        return smart_unicode(self.procedure_id)

class EndoPolyp(models.Model):
    polyp_id = models.AutoField(primary_key=True)
    procedure_id = models.ForeignKey('Procedure',related_name='polyps',on_delete=models.CASCADE,null=True)
    size = models.IntegerField()
    removed_flag = models.BooleanField()
    removed_by_equipment = models.BooleanField()
    location = models.CharField(max_length=500)
    morphology = models.CharField(max_length=100)
    scope_length_marker = models.IntegerField()
    pathalogy_indicator = models.CharField(max_length=200)

    class Meta:
        managed = True
        app_label = 'procedure'
        db_table = 'endo_polyp'
        verbose_name = _("Polyp")
    def __str__(self):
        return smart_unicode(self.polyp_id)

class EndoCenter(models.Model):
    center_id = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=255)
    room_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'endo_center'

    def __str__(self):
        return smart_unicode(self.center_name)   


class EndoEquipment(models.Model):
    equipment_id = models.IntegerField(blank=True, null=True)
    equipment_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'endo_equipment'

class EndoPatient(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patient_id = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'endo_patient'

class EndoMiniclip(models.Model):
    clip_id = models.BigIntegerField(primary_key=True)
    procedure = models.ForeignKey('Procedure', models.DO_NOTHING,related_name='miniclip', unique=True)
    polyp = models.ForeignKey('EndoPolyp', models.DO_NOTHING,related_name='miniclip_polyps')
    clip_link = models.CharField(max_length=500)
    equipment_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'endo_miniclip'
