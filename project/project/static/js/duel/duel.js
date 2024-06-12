// Autor: Jana Stanisavljević 0381/2021

function uzmiCookie(ime) {
    /*
    vraca vrednost cookie-a sa zadatim imenom;
    */
    var nameEQ = ime + "=";
    var cookies = document.cookie.split(';');
    for(var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.indexOf(nameEQ) === 0) {
            return decodeURIComponent(cookie.substring(nameEQ.length, cookie.length));
        }
    }
    return null;
}

function postaviCookie(ime, vrednost) {
    /*
    postavlja zadatu vrednost cookie-a sa datim imenom;
    */
    document.cookie = ime + "=" + encodeURIComponent(vrednost) + "; path=/";
}

function normalizuj(str) {
    /*
    uklanja znake punktuacije i razmake i kovertuje string u mala slova;
    menja srpsku latinicu u ascii karaktere;
    */
    str=str.replace(/&apos/g, "'");

    var serbianToAscii = {
        "č": "c",
        "ć": "c",
        "š": "s",
        "ž": "z",
        "đ": "dj"
    };

    str = str.replace(/[čćšžđ]/g, function(match) {
        return serbianToAscii[match];
    });

    str=str.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()\s]/g, "");
    str=str.replace(/\?/g, '');
    str=str.replace(/\'/g, '');

    return str;
}


function proveri() {
    /*
    proverava da li je unet tacan ili pogresan stih;
    */
    var unos = document.getElementById('unos').value;
    var stih = dohvatiTacneStihove();
    var alert = document.getElementById("alert");
    if (normalizuj(unos) == normalizuj(stih)) {
      alert.textContent = "Tačan odgovor!";

      let poeni = parseInt(uzmiCookie('poeni')) + 1;
      postaviCookie('poeni', poeni);
      postaviRezultatRunde(1);
      prikaziRezultat(true);
    }
    else {
      alert.textContent = "Pogrešan odgovor!";
      prikaziRezultat(false);
    }
  }

function pusti() {
    /*
    pusta i zaustavlja pesmu;
    */
    var audioPlayer = document.getElementById('audioPlayer');
    if (audioPlayer.paused) {
        audioPlayer.play();
    } else {
        audioPlayer.pause();
    }
}

function prikaziRezultat(sledeca) {
    /*
    prikazuje poruke o tacnom, netacnom odgovoru ili isteku vremena;
    */
    var alert = document.getElementById("alert");
    alert.style.opacity = "1";
    alert.style.display = "block";

    setTimeout(function() {
        ukloniRezultat(sledeca);
    }, 2000);
}

function ukloniRezultat(sledeca) {
    /*
    uklanja poruke o tacnom, netacnom odgovoru ili isteku vremena;
    */
    var alert = document.getElementById("alert");
    alert.style.opacity = "0";
    if(sledeca == true) sledeca_runda(false);
}

function tajmer() {
    /*
    meri i azurira svake sekunde proteklo vreme u jednoj rundi;
    kada vreme istekne, postavlja odgovarajucu poruku;
    */
    var timerElement = document.getElementById('timer');
    var sekunde = 0;

    var intervalId = setInterval(function() {
        sekunde++;
        timerElement.textContent = sekunde;

        if (sekunde >= 50) {
            timerElement.style.color = 'red';
        }

        if (sekunde >= 60) {
            clearInterval(intervalId);
            var alert = document.getElementById("alert");
            alert.textContent = "Isteklo vreme!";
            postaviRezultatRunde(0);
            prikaziRezultat(true);
        }
    }, 1000);
}

document.addEventListener('DOMContentLoaded', function() {
    tajmer();
});


function postaviRezultatRunde(rezultat) {
    /*
    za trenutnu rundu postavlja zadati rezultat (0 ili 1);
    */
    let runda = uzmiCookie('runda');
    postaviCookie('runda' + runda, rezultat)
}

