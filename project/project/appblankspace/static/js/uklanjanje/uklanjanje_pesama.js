// Autor: Andrija Tomić 0489/2021
function ukloniPesmu(pId) {
    /*Prosledjivanje id za brisanje pesme */
    document.cookie=`pesmaidbrisanje=${pId};path=/`;
    window.location.reload();

    
}
