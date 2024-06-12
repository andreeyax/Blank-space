// Autor: Andrija Tomić 0489/2021
function odabir_zanra(){
    /*Odabir kom zanru pripada pesma koju administrator zeli da ukloni */

    let options = document.getElementsByName('zanr');
    var selectedOption=null;
    for(let i = 0; i < options.length; i++) {
        if(options[i].checked) {
            selectedOption = options[i].value;
            break;
        }
    }

    if(selectedOption!=null){
        window.location.href = "/izbor_izvodjacaUklanjanje/";
        document.cookie=`odabranzanrpesmazabrisanje=${selectedOption};path=/`;
    }
    else{
        document.cookie=`odabranzanrpesmazabrisanje=0;path=/`;
    }
}