from django.contrib import admin
from procedure.models import Procedure


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ("procedure_id","start_time")
    list_filter = ("procedure_id", "start_time")


admin.site.register(Procedure, ProcedureAdmin)

