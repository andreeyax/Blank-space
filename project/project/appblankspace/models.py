# Autor: Jana Stanisavljevic 0381/2021
from django.db import models


class Korisnik(models.Model):
    """
    Sadrzi sve podatke o korisnicima. 
    Tip moze da ima vrednost ’A’, ‘B’, ‘S’ ili ‘M’ (Admin, Brucos, Student, Master).
    Ako je tip ’A’, polja nakon odgovor_lozinka su NULL.
    """
    korisnicko_ime = models.CharField(max_length=31)
    sifra = models.CharField(max_length=255)
    ime = models.CharField(max_length=31)
    prezime = models.CharField(max_length=31)
    tip = models.CharField(max_length=1)
    pitanje_lozinka = models.CharField(max_length=255)
    odgovor_lozinka = models.CharField(max_length=255)
    # dole navedena polja su null ako je tip 'A'
    rang_poeni = models.IntegerField(null=True)
    licni_poeni = models.IntegerField(null=True)
    poslednja_aktivnost = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'korisnik'


class Zanr(models.Model):
    """
    Sadrzi podatke o zanrovima.
    """
    naziv = models.CharField(max_length=31)

    class Meta:
        managed = True
        db_table = 'zanr'


class Izvodjac(models.Model):
    """
    Sadrzi podatke o izvodjacima.
    Povezane klase: :model:`appBlankSpace.Zanr`
    """
    ime = models.CharField(max_length=31)
    zan = models.ForeignKey(Zanr, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'izvodjac'


class Pesma(models.Model):
    """
    Sadrzi podatke o pesmama.
    Povezane klase: :model:`appBlankSpace.Izvodjac`
    """
    naziv = models.CharField(max_length=63)
    izv = models.ForeignKey(Izvodjac, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'pesma'


class Stihovi(models.Model):
    """
    Sadrzi podatke o stihovima.
    Poznat tekst je onaj koji se prikazuje igracu, a nepoznat onaj koji igrac treba da pogodi.
    Nivo moze da ima vrednost ‘E’, ‘N’ ili ‘H’ (easy, normal, hard).
    Zvuk je naziv fajla sa delom pesme.
    Povezane klase: :model:`appBlankSpace.Pesma`
    """
    nivo = models.CharField(max_length=1)
    pes = models.ForeignKey(Pesma, on_delete=models.CASCADE)
    poznat_tekst = models.CharField(max_length=255)
    nepoznat_tekst = models.CharField(max_length=255)
    zvuk = models.FilePathField()

    class Meta:
            managed = True
            db_table = 'stihovi'


class Soba(models.Model):
    """
    Sadrzi id korisnika koji je generisao sifru sobe, a kasnije se dodaje id onoga ko se pridruzio.
    Id korisnika je null ako je u pitanju neregistrovani korisnik.
    Cuva se i ukupan broj poena i osvojeni poeni u svakoj rundi (string koji predstavlja niz 0 ili 1) za oba korisnika.
    Stihovi su string koji predstavlja niz id stihova koji su izabrani za dati duel.
    Poeni = -1 oznacava da je igrac prisutan i da nije zavrsio igru (zato poeni_1 ne mogu biti null, a poeni_2 mogu).
    Povezane klase: :model:`appBlankSpace.Korisnik`
    """
    kor_1 = models.ForeignKey(Korisnik, on_delete=models.CASCADE, related_name='soba_kor_1', null=True)
    kor_2 = models.ForeignKey(Korisnik, on_delete=models.CASCADE, related_name='soba_kor_2', null=True)
    poeni_1 = models.IntegerField()
    poeni_2 = models.IntegerField(null=True)
    poeni_runde_1 = models.CharField(max_length=31, null=True)
    poeni_runde_2 = models.CharField(max_length=31, null=True)
    stihovi = models.CharField(max_length=63)

    class Meta:
            managed = True
            db_table = 'soba'


class Predlaze_Izvodjaca(models.Model):
    """
    Sadrzi podatke o trenutnim predlozima izvodjaca (onima koji nisu jos prihvaceni ili odbijeni).
    Povezane klase: :model:`appBlankSpace.Korisnik`, :model:`appBlankSpace.Zanr`
    """
    ime_izvodjaca = models.CharField(max_length=31)
    kor = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    zan = models.ForeignKey(Zanr, on_delete=models.CASCADE)

    class Meta:
            managed = True
            db_table = 'predlaze_izvodjaca'


class Predlaze_Pesmu(models.Model):
    """
    Sadrzi podatke o trenutnim predlozima pesama (onima koji nisu jos prihvaceni ili odbijeni).
    Povezane klase: :model:`appBlankSpace.Korisnik`, :model:`appBlankSpace.Izvodjac`
    """
    naziv_pesme = models.CharField(max_length=63)
    kor = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    izv = models.ForeignKey(Izvodjac, on_delete=models.CASCADE)

    class Meta:
            managed = True
            db_table = 'predlaze_pesmu'
