var data= document.getElementById('inpArea').value;

if(data)
{
    document.getElementById('paste').style.visibility='hidden';
    document.querySelector(".upl").style.visibility='hidden';
    
}

function hide()
{
    document.getElementById('paste').style.visibility='hidden';
    document.querySelector(".upl").style.visibility='hidden';
}

function myFunction() {
    var copyText = document.getElementById("myOutput");

    navigator.clipboard.writeText(copyText.value);
}

  
function pasteFunction()
{
    var paste = document.getElementById('paste');
    var pasteArea = document.getElementById('inpArea');
    
    addEventListener("click", function (){
        if(navigator.clipboard.readText().then(clipText => pasteArea.innerText = clipText));
    }) 

    paste.style.visibility='hidden';
    document.querySelector(".upl").style.visibility='hidden';

    
    
}







    


