from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.utils.encoding import smart_text as smart_unicode
from django.utils.translation import ugettext_lazy as _


class Procedure(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    procedure_id = models.CharField(_("Procedure Id"), max_length=255,null=True)
    room_id = models.IntegerField(null=True)
    start_time = models.DateTimeField(null=True)
    cecum_time = models.DateTimeField(null=True)
    inside_time = models.DateTimeField(null=True)
    stop_time = models.DateTimeField(null=True)
    class Meta:
        verbose_name = _("Procedure")
        verbose_name_plural = _("Procedures")

    def __unicode__(self):
        return smart_unicode(self.procedure_id)

