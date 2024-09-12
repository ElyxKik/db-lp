from django.db import models
from django.db.models.deletion import CASCADE



class VolumeMutalise(models.Model):
    terminal = models.CharField(max_length=200)
    volume_gasoil = models.FloatField(default=0)
    volume_essence = models.FloatField(default=0)
    volume_petrol = models.FloatField(default=0)

    class Month(models.TextChoices):
        JANVIER = 'Janvier'
        FEVRIER = 'Février'
        MARS = 'Mars'
        AVRIL = 'Avril'
        MAI = 'Mai'
        JUIN = 'Juin'
        JUILLET = 'Juillet'
        AOUT = 'Août'
        SEPTEMBRE = 'Septembre'
        OCTOBRE = 'Octobre'
        NOVEMBRE = 'Novembre'
        DECEMBRE = 'Décembre'
    
    mois = models.CharField(max_length=10, choices=Month.choices, default=Month.JANVIER)
    annee = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.mois




