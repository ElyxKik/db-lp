# Generated by Django 5.1.1 on 2024-09-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_volumemutalise_mois_alter_volumemutalise_annee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volumemutalise',
            name='volume_essence',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='volumemutalise',
            name='volume_gasoil',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='volumemutalise',
            name='volume_petrol',
            field=models.FloatField(default=0),
        ),
    ]
