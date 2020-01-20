from django.contrib import admin
from procedure.models import Procedure, EndoPolyp, EndoMiniclip,EndoCenter


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ("procedure_id","start_time")
    list_filter = ("procedure_id", "start_time")


admin.site.register(Procedure, ProcedureAdmin)

admin.site.register(EndoPolyp,admin.ModelAdmin)
admin.site.register(EndoMiniclip,admin.ModelAdmin)
admin.site.register(EndoCenter,admin.ModelAdmin)


