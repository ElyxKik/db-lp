from django.shortcuts import render
from .models import VolumeMutalise
from django.db.models import Sum

def home(request):
    # Filtre par mois et année
    mois = request.GET.get('mois')
    annee = request.GET.get('annee')

    volumes = VolumeMutalise.objects.all()

    if mois:
        volumes = volumes.filter(mois=mois)

    if annee:
        volumes = volumes.filter(annee=annee)

    # Agrégation des volumes
    total_volume_essence = volumes.aggregate(Sum('volume_essence'))['volume_essence__sum'] or 0
    total_volume_gasoil = volumes.aggregate(Sum('volume_gasoil'))['volume_gasoil__sum'] or 0
    total_volume_petrol = volumes.aggregate(Sum('volume_petrol'))['volume_petrol__sum'] or 0

    # Volume par terminal
    terminal_data = volumes.values('terminal').annotate(
        total_volume_essence=Sum('volume_essence'),
        total_volume_gasoil=Sum('volume_gasoil'),
        total_volume_petrol=Sum('volume_petrol')
    )
    # Calculer les volumes par terminal
    volumes_par_terminal = volumes.values('terminal').annotate(
        total_volume_essence=Sum('volume_essence'),
        total_volume_gasoil=Sum('volume_gasoil'),
        total_volume_petrol=Sum('volume_petrol')
    )

    # Récupérer les options de mois et d'année pour les filtres
    mois_list = VolumeMutalise.Month.choices
    annee_list = VolumeMutalise.objects.values_list('annee', flat=True).distinct()

    # Passer les données au contexte
    context = {
        'total_volume_essence': total_volume_essence,
        'total_volume_gasoil': total_volume_gasoil,
        'total_volume_petrol': total_volume_petrol,
        'volumes_par_terminal': volumes_par_terminal,
        'mois_list': mois_list,
        'annee_list': annee_list,
    }
    return render(request, 'home.html', context)