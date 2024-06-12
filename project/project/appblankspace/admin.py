from django.contrib import admin
from .models import Korisnik, Zanr, Izvodjac, Pesma, Predlaze_Izvodjaca, Predlaze_Pesmu, Soba, Stihovi

# Register your models here.
admin.site.register(Korisnik)
admin.site.register(Zanr)
admin.site.register(Izvodjac)
admin.site.register(Pesma)
admin.site.register(Predlaze_Izvodjaca)
admin.site.register(Predlaze_Pesmu)
admin.site.register(Soba)
admin.site.register(Stihovi)