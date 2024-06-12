//Autor: Maša Nikolić 0439/2021

function izbor_zanra() {
    // Funkcija koja se poziva prilikom odabira zanra i zatim se cuva kao cookie
    if(document.querySelector('input[name="zanr"]:checked')==null){
        alert("Niste selektovali zanr")
        return;
    }
    let selektovanZanr = document.querySelector('input[name="zanr"]:checked').value;

    document.cookie = "selectedGenre=" + encodeURIComponent(selektovanZanr) + ";path=/";
    var tip="DodajPesmu"
    document.cookie= "tipDodavanja="+encodeURIComponent(tip)+";path=/";
    window.location.href = "/izbor_izvodjaca/";
}

function izbor_izvodjaca(){
    // Funkcija koja se poziva prilikom odabira izvodjaca i zatim se cuka kao cookie
    if(document.querySelector('input[name="izv"]:checked')==null){
        alert("Niste selektovali izvodjaca")
        return;
    }
    let selectedValue = document.querySelector('input[name="izv"]:checked').value;
    document.cookie = "selectedIzvodjac=" + encodeURIComponent(selectedValue) + ";path=/";
    window.location.href = "/pesma_podaci/";
}

function izbor_zanra2(){
    // Funkcija koja se poziva prilikom odabira zanra i zatim se cuva kao cookie
    if(document.querySelector('input[name="zanr"]:checked')==null){
        alert("Niste selektovali zanr")
        return;
    }
    let selectedValue = document.querySelector('input[name="zanr"]:checked').value;
    
    document.cookie = "selectedGenre=" + encodeURIComponent(selectedValue) + ";path=/";
    var tip="DodajIzvodjaca"
    document.cookie= "tipDodavanja="+encodeURIComponent(tip)+";path=/";
    window.location.href = "/ime_izvodjaca/";
}

function ime_izvodjaca_kolacic(){
    // Postavlja se kolacic sa imenom izvodjaca
    var ime = document.getElementById('ime').value;
    if(ime==null){
        alert("Niste uneli podatak")
        return;
    }
    document.cookie = "postavljenoImeIzvodjaca=" + encodeURIComponent(ime) + ";path=/";
    window.location.href = "/pesma_podaci/";
}


function postaviKolacicDodajZanr(){
    alert('sdafasdfwwww')
    let naziv = document.getElementById('naziv').value;
    console.log(naziv)
    if (naziv == "") {
        alert('Niste uneli naziv žanra!');
        return false;
    }
    if(naziv=="rok"){
        alert('Niste unelirok!');
        return false;
    }
    document.cookie = "postavljenZanr=" + naziv + ";path=/";
    
    //window.location.href="/ime_izvodjaca/"

    var tip="DodajZanr"
    document.cookie= "tipDodavanja="+encodeURIComponent(tip)+";path=/";
    //window.location.href="/ime_izvodjaca/"
    return true;
}


function pesma_podaci_citanje(){
    //const fileInput = document.getElementById('fileInput');
    //const files = fileInput.files;
    
    alert("greska")
    if (files.length === 0) {
        alert('Niste uneli fajl sa zvukom!');
        return;
    }
    if(document.getElementById('stihovi1').value == "" || document.getElementById('stihovi2').value == "") {
        alert('Niste uneli stihove!');
        return;
    }
    var naziv = document.getElementById('naziv').value;
    var stihovi1=document.getElementById('stihovi1').value;
    var stihovi2=document.getElementById('stihovi2').value;
    form.submit()
    
    //dodati nivo
    var radioDugmad = document.getElementsByName('nivo');
    var nivo;
    for (let i = 0; i < radioDugmad.length; i++) {
        if (radioDugmad[i].checked) {
            nivo=radioDugmad[i].value;
            break;
        }
    }

    window.location.href = "/pesma_podaci/dodavanje/"+naziv+"/"+stihovi1+"/"+stihovi2+"/"+nivo+"/";         
}

function validateForm(event) {
    if(document.getElementById('stihovi1').value == "" || document.getElementById('stihovi2').value == "") {
      alert('Niste uneli stihove! asdf');
      return false;
    }
    return true; // Form is valid
  }