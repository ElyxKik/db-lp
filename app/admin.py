from django.contrib import admin
from app.models import VolumeMutalise



class VolumeMutaliseAdmin(admin.ModelAdmin):
    list_display = ('terminal','volume_gasoil', 'volume_essence','volume_petrol', 'mois', 'annee')




admin.site.register(VolumeMutalise, VolumeMutaliseAdmin)
