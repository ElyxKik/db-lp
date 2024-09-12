from django.db import models
from django.db.models.deletion import CASCADE
from decimal import Decimal



class VolumeMutalise(models.Model):
    terminal = models.CharField(max_length=200)
    volume_gasoil = models.DecimalField(max_digits=10, decimal_places=3, default=Decimal('0.000'))
    volume_essence = models.DecimalField(max_digits=10, decimal_places=3, default=Decimal('0.000'))
    volume_petrol = models.DecimalField(max_digits=10, decimal_places=3, default=Decimal('0.000'))

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




