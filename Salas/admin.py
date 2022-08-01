from django.contrib import admin
from .models import *

class ComputadorAdmin(admin.ModelAdmin):
    list_display = ( "sala", "sistemaOperativo","ip","mac", "mascaraSubRed","procesador","memoriRam", "estadoPC", "fechaInstalacion")
    search_fields = ("sistemaOperativo", "ip")
    list_filter = ("sistemaOperativo","procesador",)

class SalasAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipoDeSalas","sede","piso","estadoSala","wifi")
    list_filter = ("tipoDeSalas","sede")
    search_fields = ("nombre",)

class SedeAdmin(admin.ModelAdmin):
    list_display= ("nombre","calle","numero")

class MonitorAdmin(admin.ModelAdmin):
    list_display= ("marca","tamaño","sala")


admin.site.register(Sede,SedeAdmin)
admin.site.register(Sala,SalasAdmin)
admin.site.register(Computador,ComputadorAdmin)
#admin.site.register(Procesador)
#admin.site.register(memoriaRam)
admin.site.register(Monitor,MonitorAdmin)
admin.site.register(Proyector)
admin.site.register(Sonido)
admin.site.register(Telon)