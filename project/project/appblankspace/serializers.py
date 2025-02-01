# Maša Nikolić 0439/2021

# serializers.py
from rest_framework import serializers
from .models import *

class ZanrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zanr
        fields = ['id', 'naziv']

class IzvodjacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izvodjac
        fields = ['id', 'ime','zan_id']

class RangListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['korisnicko_ime','rang_poeni']

class MojProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['ime','prezime','korisnicko_ime','licni_poeni','rang_poeni']


class StihSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stihovi
        fields = ['id', 'pozant_tekst', 'nepoznat_tekst', 'zvuk']

class PesmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesma
        fields = ['id', 'naziv']

class IzvodjacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izvodjac
        fields = ['id', 'ime']

class PesmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesma
        fields = ['id', 'naziv']

class KorisnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['ime','korisnicko_ime','tip']

class KorisnikUklanjanjeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['korisnicko_ime','poslednja_aktivnost']

class KorisnikZaboravljenaLozinkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = ['korisnicko_ime','pitanje_lozinka','odgovor_lozinka','tip']

class PredlazeIzvodjacaSerializer(serializers.ModelSerializer):
    # Korisničko ime kao string
    kor_ime = serializers.CharField(source='kor.korisnicko_ime', read_only=True)
    # Žanr kao string
    zan_naziv = serializers.CharField(source='zan.naziv', read_only=True)
    
    # Polje koje nije deo modela, dodajemo ga ručno
    odgovor = serializers.SerializerMethodField()

    class Meta:
        model = Predlaze_Izvodjaca
        fields = ['id','ime_izvodjaca', 'kor_ime', 'zan_naziv', 'odgovor']

    def get_odgovor(self, obj):
        return "Nema novih predloga" if Predlaze_Izvodjaca.objects.count() == 0 else "Uspešno učitano"

class PredlazePesmaSerializer(serializers.ModelSerializer):
    kor_ime = serializers.CharField(source='kor.korisnicko_ime', read_only=True)
    zan_naziv = serializers.CharField(source='izv.zan.naziv', read_only=True)
    izv_ime = serializers.CharField(source="izv.ime", read_only=True)
    
    odgovor = serializers.SerializerMethodField()

    class Meta:
        model = Predlaze_Pesmu
        fields = ['id','naziv_pesme','izv_ime', 'kor_ime', 'zan_naziv', 'odgovor']

    def get_odgovor(self, obj):
        return "Nema novih predloga" if Predlaze_Izvodjaca.objects.count() == 0 else "Uspešno učitano"