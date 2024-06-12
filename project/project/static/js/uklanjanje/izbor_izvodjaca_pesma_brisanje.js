// Autor: Andrija Tomić 0489/2021
function odabir_izvodjaca(){
    /*Odabir kom izvodjacu pripada pesma koju administrator zeli da ukloni */
    let options = document.getElementsByName('zanr');
    var selectedOption=null;


    
    for(let i = 0; i < options.length; i++) {
        if(options[i].checked) {
            selectedOption = options[i].value;
            break;
        }
    }

    if(selectedOption!=null){
        window.location.href = "/uklanjanje_pesama/";
        document.cookie=`odabranizvodjacpesmazabrisanje=${selectedOption};path=/`;
    }
    else{
        document.cookie=`odabranizvodjacpesmazabrisanje=0;path=/`;
    }
}