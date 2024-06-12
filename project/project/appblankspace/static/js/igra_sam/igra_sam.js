// Autor: Andrija Tomić 0489/2021

let radi=false;

function pusti(){
        
    var audioPlayer = document.getElementById("audioPlayer");
    if (audioPlayer.paused) {
        audioPlayer.play();
    } else {
        audioPlayer.pause();
    }
}

function ididalje(){
    var runda = document.cookie.split(';').find(cookie => cookie.trim().startsWith("runda_igra_sam" + '='));
    var runda1=null
    if (runda) {
        runda1 = parseInt(runda.split('=')[1]);
    }

    if(runda1==7){
        runda=0;
        document.cookie="runda_igra_sam="+runda+";path=/";
        window.location.href="/kraj_igre/";
        return;

    }
    else{

        document.cookie="runda_igra_sam="+runda1+";path=/";
        window.location.href="/igra_sam/"
    }


    

}



function tekst(tacno){

    if(radi){
        return;
    }
    radi=true;

    let x=('{{crtice}}');
    x.split("  ");
    crte=document.getElementById("tekst").innerHTML;
    crte=crte.split("<br>");
    tacno=tacno.replace(/&apos/g, "'");
    tacnoreci=tacno.split(" ");
    let prvaSlova = tacnoreci.map(rec => rec[0]);
    let j=crte.length-1;
    niz=crte[j].split("&nbsp;");
    
    let k=0;

    for(let x=0;x<niz.length;x++){
        if(x==0){
            niz[x]="\n            \n\n            "+prvaSlova[k];
            ++k;
        }
        if(niz[x]=="  _"){
            niz[x]="&nbsp;&nbsp;"+prvaSlova[k];
            ++k;
        }
    }

    crte[j]=niz.join('  ');
    crte=crte.join("<br>");
    document.getElementById("tekst").innerHTML=crte;


}

function pesma(pesma){
    document.getElementById("ispisporuka").style.color="rgb(73, 0, 107)";
    document.getElementById("ispisporuka").style.fontSize='30px';
    document.getElementById("ispisporuka").innerHTML=pesma;
}

$(document).ready(function(){
    document.getElementById("unos").textContent=""

    let sekunde=0;
    var runda = document.cookie.split(';').find(cookie => cookie.trim().startsWith("runda_igra_sam" + '='));
    var runda1=null
    if (runda) {
        runda1 = parseInt(runda.split('=')[1]);
        
    }
    
    let r=document.getElementById("rundaVreme").value;
    document.getElementById("rundaVreme").innerHTML='Runda: '+ runda1+'&ensp;&ensp;Vreme: '+'<span id="timer">'+sekunde+'</span>';
   
    var cookieValue = document.cookie.split(';').find(cookie => cookie.includes('runda_igra_sam'));
    var cookieValue1=null;
    if (cookieValue) {
    
        var runda = parseInt(cookieValue.split('=')[1]);
        
        if(runda==0 && sekunde==0){
            document.cookie="bile_pesme="+""+";path=/";
            let t=0
            document.cookie="poeni_igra_sam="+t+";path=/";
            
        }
        
    }
    
    var poeni = document.cookie.split(';').find(cookie => cookie.trim().startsWith("poeni_igra_sam" + '='));
    var poeni1=null
    if (poeni) {
        poeni1 = parseInt(poeni.split('=')[1]);
        
    }
   
    document.cookie="poeni_igra_sam="+poeni1+";path=/";
    document.getElementById("score").innerHTML=poeni1+"&ensp;&#119070";


    
    

    let i=setInterval(function(){
        sekunde+=1;
        var runda = document.cookie.split(';').find(cookie => cookie.trim().startsWith("runda_igra_sam" + '='));
        var runda1=null
        if (runda) {
            runda1 = parseInt(runda.split('=')[1]);
            
        }

        console.log(runda1)
        
        let r=document.getElementById("rundaVreme").value;
        r=r-1;
        document.getElementById("rundaVreme").innerHTML='Runda: '+runda1+'&ensp;&ensp;Vreme: '+'<span id="timer">'+sekunde+'</span>';
        if(sekunde>=50){
            document.getElementById("timer").style.color="red";
        }

        

        if(sekunde==60){
            var cookieValue = document.cookie.split(';').find(cookie => cookie.includes('runda_igra_sam'));
            if (cookieValue) {
                runda = parseInt(cookieValue.split('=')[1]);
                if(runda==7){

                    runda=0;
                    document.cookie="runda_igra_sam="+runda+";path=/";
                    clearInterval(i);
                    window.location.href="/kraj_igre/";
                    return;
                }
                document.cookie="runda_igra_sam="+runda+";path=/";
            }
            window.location.reload();

        }
            
    },1000)


});

function proveri(tacno){
    let moje=document.getElementById("unos").value
    moje=moje.replace(/&apos/g, "'");
    tacno=tacno.replace(/&apos/g, "'");

    var serbianToAscii = {
        "č": "c",
        "ć": "c",
        "š": "s",
        "ž": "z",
        "đ": "dj"
    };

    tacno = tacno.replace(/[čćšžđ]/g, function(match) {
        return serbianToAscii[match];
    });

    tacno=tacno.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()\s]/g, "");
    
    
    
    moje = moje.replace(/[čćšžđ]/g, function(match) {
        return serbianToAscii[match];
    });

    moje=moje.toLowerCase().replace(/[.,\/#!$%\^&\*;:{}=\-_`~()\s]/g, "");

    moje=moje.replace(/\'/g, '');
    tacno=tacno.replace(/\'/g, '');

    moje=moje.replace(/\?/g, '');
    tacno=tacno.replace(/\?/g, '');
    
    if(moje==tacno){
        var poeni = document.cookie.split(';').find(cookie => cookie.trim().startsWith("poeni_igra_sam" + '='));
        var poeni1=null
        if (poeni) {
            var poeni1 = parseInt(poeni.split('=')[1]);
            
        }
        poeni1++;
        document.cookie="poeni_igra_sam="+poeni1+";path=/";
        
        document.getElementById("score").innerHTML=poeni1+"&ensp;&#119070";

        
        document.getElementById("ispisporuka").textContent="Tačan odgovor!";
        document.getElementById("ispisporuka").style.color="rgb(100, 150, 100)";
        document.getElementById("ispisporuka").style.fontSize="30px";

        
        setInterval(function(){

           
            var runda = document.cookie.split(';').find(cookie => cookie.trim().startsWith("runda_igra_sam" + '='));
            var runda1=null
            if (runda) {
                runda1 = parseInt(runda.split('=')[1]);
                
            }
            
            if(runda1==7){
                runda=0;
                document.cookie="runda_igra_sam="+runda+";path=/";
                window.location.href="/kraj_igre/";
                return;

            }
            document.cookie="runda_igra_sam="+runda1+";path=/";
            window.location.reload();
        },1000)
        
        
        
    }
    else{
        document.getElementById("ispisporuka").textContent="Netačan odgovor";
        document.getElementById("ispisporuka").style.color="red";
        document.getElementById("ispisporuka").style.fontSize="30px";
        setTimeout(function(){
            document.getElementById("ispisporuka").textContent="";
            
        },1000);
    }

}


function izvodjac(izvodjac){
    document.getElementById("ispisporuka").style.color="rgb(73, 0, 107)";
    document.getElementById("ispisporuka").style.fontSize='30px';
    document.getElementById("ispisporuka").innerHTML=izvodjac;
}



    


