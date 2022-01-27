var inicio = new Date().getTime();  //Alcance global

function obtenerColorAleatorio()
{
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++)
    {
        color += letters[Math.round(Math.random() * 15)];
    }
    return color;
}

function aparecerForma()
{
    var top  = Math.random()*400 + "px";
    var left = Math.random()*400 + "px";
    var width = (Math.random()*200)+100 + "px";
    var colorAleatorio = obtenerColorAleatorio();

    if(Math.random() > 0,5)
    {
        document.getElementById("forma").style.borderRadius = "50%";
    }
    else
    {
        document.getElementById("forma").style.borderRadius = "0%";
    }

    document.getElementById("forma").style.display = "block";
    document.getElementById("forma").style.top = top;
    document.getElementById("forma").style.left = left;
    document.getElementById("forma").style.width = width;
    document.getElementById("forma").style.height = width;
    document.getElementById("forma").style.backgroundColor = colorAleatorio;

    inicio = new Date().getTime();
    obtenerColorAleatorio();
}

function aparecerFormaDespuesRetraso()
{
    setTimeout(aparecerForma, Math.random()*2000);
}

document.getElementById("forma").onclick = function()
{
    document.getElementById("forma").style.display = "none";
    var fin = new Date().getTime();
    var diferencia = (fin - inicio)/1000;
    document.getElementById("tiempoReaccion").innerHTML = diferencia + "s"
    aparecerFormaDespuesRetraso();
}