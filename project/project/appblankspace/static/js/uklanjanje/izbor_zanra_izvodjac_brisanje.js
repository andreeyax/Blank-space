// Autor: Andrija Tomić 0489/2021
function izbor_zanra_brisanje(){

    /*Odabir kom zanru pripada izvodjac kog administrator zeli da ukloni */
    let options = document.getElementsByName('zanr');
    var selectedOption=null;


    let flag 
    for(let i = 0; i < options.length; i++) {
        if(options[i].checked) {
            selectedOption = options[i].value;
            break;
        }
    }


    

    if(selectedOption!=null){
        window.location.href = "/uklanjanje_izvodjaca/";
        document.cookie=`odabranzanrizvodjacazabrisanje=${selectedOption};path=/`;
    }
    else{
        document.cookie=`odabranzanrizvodjacazabrisanje=0;path=/`;
    }

    


}