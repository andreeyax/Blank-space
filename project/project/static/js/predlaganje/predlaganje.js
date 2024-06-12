//Autor: Maša Nikolić 0439/2021

function predlozi(){
    var ime = document.getElementById('ime').value;
    let zanr = document.querySelector('input[name="zanr"]:checked');
    if(zanr==null && ime!=""){
        alert("Niste selektovali zanr")
        return;
    }
    else if(ime=="" && zanr!=null){
        alert("Niste uneli ime izvodjaca")
        return;
    }
    else if(ime=="" && zanr==null){
        alert("Niste uneli sve podatke!");
        return;
    }
    let selektovanZanr = document.querySelector('input[name="zanr"]:checked').value;
    //alert("Uspesno dodat predlog")
    window.location.href="/predlaganje_izvodjaca/dodaj_predlog_izvodjaca/"+ime+"/"+selektovanZanr;
}

function predlog_pesme(){
    var pesma = document.getElementById('pesma').value;
    let zanr = document.querySelector('input[name="zanr"]:checked');
    let izvodjac = document.getElementById('izvodjac');
    
    if(pesma == "" && zanr!=null && izvodjac!=null) {
        alert("Niste uneli ime pesme");
        return;
    }
    else if(pesma != "" && zanr==null && izvodjac!=null) {
        alert("Niste selektovali zanr pesme");
        return;
    }
    else if(pesma != "" && zanr!=null && izvodjac==null) {
        alert("Niste selektovali ime izvodjaca");
        return;
    }
    else if(pesma == "" || zanr==null || izvodjac==null) {
        alert("Niste uneli sve podatke");
        return;
    }
    let selektovanZanr = document.querySelector('input[name="zanr"]:checked').value;
    let selektovanIzvodjac = document.getElementById('izvodjac').value;
    //alert("Uspesno dodat predlog")
    window.location.href = "/predlaganje_pesama/dodaj_predlog_pesme/"+pesma+"/"+selektovanIzvodjac+"/"+selektovanZanr;
}