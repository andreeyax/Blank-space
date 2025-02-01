from django.urls import include, path
from . import views
from django.contrib import admin
from .viewsM import *

urlpatterns = [

    # pocetne putanje
    path('', views.pocetna,name='pocetna'),
    path('pocetna_brucos/', views.pocetna_brucos,name='pocetna_brucos'),
    path('pocetna_administrator/', views.pocetna_administrator,name='pocetna_administrator'),
    path('pocetna_master/', views.pocetna_master,name='pocetna_master'),
    path('pocetna_student/', views.pocetna_student,name='pocetna_student'),
    path('vrati_na_pocetnu', views.vrati_na_pocetnu, name='vrati_na_pocetnu'),
    path('logout', views.logout, name='logout'),

    # igra sam putanje
    path('igra_sam/',views.igra_sam,name='igra_sam'),
    path('nivo/',views.nivo,name='nivo'),
    path('zanr/',views.zanr,name='zanr'),
    path('kraj_igre/',views.kraj_igre,name='kraj_igre'),
    
    # autorizacija putanje
    path('login/', views.login, name='login'),
    path('forgotpass/',views.forgotpass,name='forgotpass'),
    path('forgotpassq/',views.forgotpassq,name='forgotpassq'),
    path('correctUser/',views.correctUser, name='correctUser'),
    path('newpass/',views.newpass,name='newpass'),
    path('registration/',views.registration,name='registration'),

    path('pravila_igre/',views.pravila_igre,name='pravila_igre'),
    path('pregled_profila/',views.pregled_profila,name='pregled_profila'),
    path('rang_lista/',views.rang_lista,name='rang_lista'),

    # predlozi, dodavanje, uklanjanje putanje
    path('predlozi_pesama/',views.predlozi_pesama,name='predlozi_pesama'),
    path('predlaganje_pesama/',views.predlaganje_pesama,name='predlaganje_pesama'),
    path('predlaganje_izvodjaca/',views.predlaganje_izvodjaca,name='predlaganje_izvodjaca'),
    path('naziv_zanra/',views.naziv_zanra,name='naziv_zanra'),
    path('ime_izvodjaca/',views.ime_izvodjaca,name='ime_izvodjaca'),
    path('izbor_izvodjaca/',views.izbor_izvodjaca,name='izbor_izvodjaca'),
    path('izbor_zanra1/', views.izbor_zanra1, name='izbor_zanra1'),
    path('izbor_zanra2/', views.izbor_zanra2, name='izbor_zanra2'),
    path('predlozi_izvodjaca/',views.predlozi_izvodjaca,name='predlozi_izvodjaca'),
    path('pesma_podaci/',views.pesma_podaci,name='pesma_podaci'),
    path('pesma_podaci1/',views.pesma_podaci1,name='pesma_podaci1'),
    path('izbor_izvodjacaUklanjanje/',views.izbor_izvodjacaUklanjanje,name='izbor_izvodjacaUklanjanje'),
    path('uklanjanje_zanrova/',views.uklanjanje_zanrova,name='uklanjanje_zanrova'),
    path('izbor_zanra1Uklanjanje/',views.izbor_zanra1Uklanjanje,name='izbor_zanra1Uklanjanje'),
    path('izbor_zanra2Uklanjanje/',views.izbor_zanra2Uklanjanje,name='izbor_zanra2Uklanjanje'),
    path('uklanjanje_pesama/',views.uklanjanje_pesama,name='uklanjanje_pesama'),
    path('uklanjanje_korisnika/',views.uklanjanje_korisnika,name='uklanjanje_korisnika'),
    path('uklanjanje_izvodjaca/',views.uklanjanje_izvodjaca,name='uklanjanje_izvodjaca'),

    #duel putanje
    path('duel/',views.duel,name='duel'),
    path('kraj_duela/',views.kraj_duela,name='kraj_duela'),
    path('cekanje_rezultata/',views.cekanje_rezultata,name='cekanje_rezultata'),
    path('sifra_sobe/',views.sifra_sobe,name='sifra_sobe'),
    path('generisi_sifru_sobe/',views.generisi_sifru,name='generisi_sifru_sobe'),
    path('proveri_sifru_sobe/',views.proveri_sifru,name='proveri_sifru_sobe'),
    path('stigao_igrac/',views.stigao_igrac,name='stigao_igrac'),
    path('zavrsio_igrac/',views.zavrsio_igrac,name='zavrsio_igrac'),


    #predlozi putanje
    path('predlozi_izvodjaca/obrisi_podatak/<int:id>/',views.obrisi_podatak,name='obrisi_podatak'),
    path('predlozi_izvodjaca/prihvati_predlog/<int:id>/<int:zan_id>/<int:kor_id>',views.prihvati_predlog,name='prihvati_predlog'),
    path('predlozi_pesama/prihvati_predlog_pesme/<int:id>/',views.prihvati_predlog_pesme,name='prihvati_predlog_pesme'),
    path('predlozi_pesama/obrisi_podatak_pesme/<int:id>/',views.obrisi_podatak_pesme,name='obrisi_podatak_pesme'),

    path('pesma_podaci1/dodavanje/',views.pesma_podaci_dodavanje,name='pesma_podaci_dodavanje'),
    path('predlozi_pesama_kolacici/<int:id>/<str:naziv>/<str:ime>/<str:zanr>/<str:korime>/',views.predlozi_pesama_kolacici,name='predlozi_pesama_kolacici'),
    path('pesma_podaci/dodavanje/',views.pesma_podaci_dodavanje_dodaj,name='pesma_podaci_dodavanje_dodaj'),
   

    #predlaganje putanje
    path('predlaganje_izvodjaca/dodaj_predlog_izvodjaca/<str:ime>/<int:zanr>',views.dodaj_predlog_izvodjaca,name='dodaj_predlog_izvodjaca'),
    path('predlaganje_pesama/dodaj_predlog_pesme/<str:pesma>/<str:ime>/<str:zanr>',views.dodaj_predlog_pesme,name='dodaj_predlog_pesme'),
    path('pocetnaUlogovanTip/',views.pocetnaUlogovanTip,name="pocetnaUlogovanTip"),


    
    # android
    path('zanrovi/', ZanrList.as_view(), name='zanr-list'),
    path('igra_sam_android/', IgraSamAPIView.as_view(), name='igra_sam_android'),
    path('kraj_igre_adndroid/', KrajIgre.as_view(), name="kraj_igre_adndroid"),
    path('rang_lista_andoid/', RangLista.as_view(), name='rang_lista_andoid'),
    path('pregled_profila_andoid/', MojProfil.as_view(), name='pregled_profila_andoid'),
    path('izvodjaci_andoid/', IzvodjaciList.as_view(), name='izvodjaci_andoid'),
    path('get_audio/',SongsApi.as_view(),name='get_audio'),
    path('login_android/',LoginApi.as_view(),name='login_android'),
    path('predlaganje_izvodjaca_android/',PredlaganjeIzvodjacaApi.as_view(),name='predlaganje_izvodjaca_android'),
    path('predlaganje_pesme_android/',PredlaganjePesmeApi.as_view(),name='predlaganje_pesme_android'),
    path('izvodjaci_zanra_andoid/', UklanjanjeZanrIzvodjaca.as_view(), name="izvodjaci_zanra_andoid"),
    path('izvodjaci_pesme_andoid/', UklanjanjePesmeIzvodjaca.as_view(), name="izvodjaci_pesme_andoid"),  
    path('uklanjanje_korisnika_android/', UklanjanjeKorisnika.as_view(), name="uklanjanje_korisnika_android"),
    path('registracija_android/', Registracija.as_view(), name="registracija_android"),
    path('zaboravljena_lozinka_android/', ZaboravljenaLozinka.as_view(), name="zaboravljena_lozinka_android"),
    path('zaboravljena_lozinka_pitanje_android/', ZaboravljenaLozinkaPitanje.as_view(), name="zaboravljena_lozinka_pitanje_android"),
    path('nova_lozinka_android/', NovaLozinka.as_view(), name="nova_lozinka_android"),
    path('predlozi_izvodjaca_android/', PredloziIzvodjaca.as_view(), name="predlozi_izvodjaca_android"),
    path('predlozi_izvodjaca_odbij_android/', PredloziIzvodjacaOdbij.as_view(), name="predlozi_izvodjaca_odbij_android"),
    path('predlozi_pesme_android/', PredloziPesme.as_view(), name="predlozi_pesme_android"),
    path('predlozi_pesme_odbij_android/', PredloziPesmeOdbij.as_view(), name="predlozi_pesme_odbij_android"),
    path('ukloni_korisnika_android/', UklanjanjeKorisnika.as_view(), name="ukloni_korisnika_android"),
    path('ukloni_zanr_android/', UklanjanjeZanraAPI.as_view(), name="ukloni_zanr_android"),
    path('ukloni_izvodjaca_android/', UklanjanjeIzvodjacaAPI.as_view(), name="ukloni_izvodjaca_android"),
    path('ukloni_pesmu_android/', UklanjanjePesmeAPI.as_view(), name="ukloni_pesmu_android"),

    path('provera_da_li_postoji/', ProveraPostojanja.as_view(), name="provera_da_li_postoji"),
    path('dodaj_zanr_android/', DodajZanrAPI.as_view(), name="dodaj_zanr_android"),

    # android duel
    path('duel_android/',DuelAPI.as_view(),name='duel_android'), 
    path('kraj_duela_android/', KrajDuelaAPI.as_view(),name='kraj_duela_android'),
    path('cekanje_rezultata_android/',CekanjeRezultataAPI.as_view(),name='cekanje_rezultata_android'),
    #path('sifra_sobe_android/',views.sifra_sobe,name='sifra_sobe_android'),
    path('generisi_sifru_sobe_android/',GenerisiSifruAPI.as_view(),name='generisi_sifru_sobe_android'), 
    path('proveri_sifru_sobe_android/',ProveriSifruAPI.as_view(),name='proveri_sifru_sobe_android'), 
    path('stigao_igrac_android/',StigaoIgracAPI.as_view(),name='stigao_igrac_android'), 
    path('zavrsio_igrac_android/',ZavrsioIgracAPI.as_view() ,name='zavrsio_igrac_android') 
]