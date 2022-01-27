// Arreglo que contiene las intrucciones del juego 
var instrucciones = ['Completá el rompecabezas según el objetivo', 'Utilizá las flechas para intercambiar una pieza con la blanca', 'Podés encontrar tus últimos 3 movimientos como ayuda'];
// Arreglo para ir guardando los movimientos que se vayan realizando
var movimientos = [];

// Representación de la grilla. Cada número representa a una pieza.
// El 9 es la posición vacía
var grilla = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
 // Grilla de ayuda con posiciones originales para revisar ganador
var grilla2 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

function flechasFinal(movimientos){
  let respuesta='';
  for(let i=0; i<movimientos.length; i++){
    switch (movimientos[i]){
      case codigosDireccion.ARRIBA:
        respuesta+= '↑ '
        break;
      case codigosDireccion.ABAJO:
        respuesta+='↓';
        break;
      case codigosDireccion.DERECHA:
        respuesta+='→ ';
        break;
      case codigosDireccion.IZQUIERDA:
        respuesta+='← '
        break;
    }
  }
  return respuesta;
}

/* Estas dos variables son para guardar la posición de la pieza vacía. 
Esta posición comienza siendo la [2, 2] Ya retornan correcto las posiciones, funciona*/
var filaVacia = 2;
var columnaVacia = 2;

/* Esta función deberá recorrer el arreglo de instrucciones pasado por parámetro. 
Cada elemento de este arreglo deberá ser mostrado en la lista con id 'lista-instrucciones'. 
Para eso deberás usar la función ya implementada mostrarInstruccionEnLista().
Podés ver su implementación en la ultima parte de este codigo. */
function mostrarInstrucciones(instrucciones) {
    for (let i=0; i<instrucciones.length;i++){
      mostrarInstruccionEnLista(instrucciones[i], 'lista-instrucciones');
    }
}

/* COMPLETAR: Crear función que agregue la última dirección al arreglo de movimientos
y utilice actualizarUltimoMovimiento para mostrarlo en pantalla */
function agregarUltMov(direccion){
  movimientos.push(direccion);
  actualizarUltimoMovimiento(direccion);
//El parámetro debería venir de la fn actualizarPosicionValida()
}

//Para recorrer y mostrar ultimos 3, hacer un for con i=array.length-1, i>=0; i--, adentro un if que refiera  a un contador si el contador es 2, break

 function ultimos3Movimientos(arreglo){
   let contador=0;
   let almacenTemporal=[]; //Almacena constantemente los últimos movimientos
   ultimoMov2 = document.getElementById('flecha2');
   ultimoMov3 = document.getElementById('flecha3');
   for(let i=arreglo.length-2; i>=0; i--){
     almacenTemporal.push(arreglo[i]);
     contador ++;
     if (contador===2){ //contador para salir del bucle
       break;
     }

   }
   // Muestra los ultimos dos movimientos en orden regresivo (primero el movimiento dos, luego el tres)
   switch (almacenTemporal[0]){
     case codigosDireccion.ARRIBA: 
       ultimoMov2.textContent = '↑';
       break;
     case codigosDireccion.ABAJO: 
       ultimoMov2.textContent = '↓';
       break;
     case codigosDireccion.DERECHA: 
       ultimoMov2.textContent = '→';
       break;
     case codigosDireccion.IZQUIERDA:
       ultimoMov2.textContent = '←';
       break;
   }
   switch (almacenTemporal[1]){ 
     case codigosDireccion.ARRIBA: 
       ultimoMov3.textContent = '↑';
       break;
     case codigosDireccion.ABAJO:
       ultimoMov3.textContent = '↓';
       break;
     case codigosDireccion.DERECHA: 
       ultimoMov3.textContent = '→';
       break;
     case codigosDireccion.IZQUIERDA: 
       ultimoMov3.textContent = '←';
       break;
   }
 }

/* Esta función va a chequear si el Rompecabezas esta en la posicion ganadora. 
Existen diferentes formas de hacer este chequeo a partir de la grilla. */
function chequearSiGano() {
  let resultado = true;
    for (let i=1; i<grilla.length; i++){
      for (let j=0; j<grilla[i].length;j++){
        if (grilla[i][j]!=grilla2[i][j]){
          resultado = false;
        }
      }
    }
    return resultado;
  }    

// Implementar alguna forma de mostrar un cartel que avise que ganaste el juego
function mostrarCartelGanador() {
    if (chequearSiGano()){
      alert("Felicitaciones! Ganaste!");
    }
    let footer= document.getElementById('footer');
    footer.className= footer.className.replace('no_mostrar', 'animacion_footer'); //Retira el display:none 
    footer.innerHTML="<h4>Movimientos ("+movimientos.length+")"+"<br><p>"+flechasFinal(movimientos)+"</p>"
}

/* Función que intercambia dos posiciones en la grilla.
Pensar como intercambiar dos posiciones en un arreglo de arreglos. 

Se te ocurre cómo solucionar esto con una variable temporal?
*/
function intercambiarPosicionesGrilla(filaPos1, columnaPos1, filaPos2, columnaPos2) {
  let auxilio1= grilla[filaPos1][columnaPos1];
  let auxilio2 = grilla[filaPos2][columnaPos2];

  grilla[filaPos1][columnaPos1] = auxilio2;
  grilla[filaPos2][columnaPos2] = auxilio1;
  //COMPLETO

  // console.log(auxilio1+' valor de la variable auxilio 1');
  // console.log(grilla[filaPos2][columnaPos2]+' pos2');
  // console.log(auxilio2+' valor de la variable auxilio 2');

}

// Actualiza la posición de la pieza vacía
function actualizarPosicionVacia(nuevaFila, nuevaColumna) {
  filaVacia = nuevaFila;
  columnaVacia = nuevaColumna;
}


// Para chequear si la posicón está dentro de la grilla. Solo devuelve true y gatilla el movimiento si la col/fila que se pasa por parámetro es menor a 2 (largo máx permitido del array) y mayor a 0 --- COMPLETO ---
function posicionValida(fila, columna) {
    let posicion = true;
    if(columna>2 || columna < 0){
          posicion = false;
        }
    if(fila>2 || fila < 0 ){
        posicion = false;      
    }

    return posicion;

}

/* Movimiento de fichas, en este caso LA QUE SE MUEVE ES LA BLANCA (!) intercambiando su posición con otro elemento.
Las direcciones están dadas por números que representa: arriba (38), abajo (40), izquierda (37), derecha (39) */
function moverEnDireccion(direccion) {
  var nuevaFilaPiezaVacia;
  var nuevaColumnaPiezaVacia;

  // Mueve pieza hacia la abajo, reemplazandola con la blanca - BLANCA SUBE
  if (direccion === codigosDireccion.ABAJO) {
    nuevaFilaPiezaVacia = filaVacia - 1;
    nuevaColumnaPiezaVacia = columnaVacia;
  }
    
  // Mueve pieza hacia arriba, reemplazandola con la blanca - BLANCA BAJA
  else if (direccion === codigosDireccion.ARRIBA) {
    nuevaFilaPiezaVacia = filaVacia + 1;
    nuevaColumnaPiezaVacia = columnaVacia;
  }
    
  // Mueve pieza hacia la derecha, reemplazandola con la blanca - BLANCA MUEVE IZQUIERDA
  else if (direccion === codigosDireccion.DERECHA) {
    nuevaFilaPiezaVacia = filaVacia;
    nuevaColumnaPiezaVacia = columnaVacia - 1;
  }
    
  // Mueve pieza hacia la izquierda, reemplazandola con la blanca - BLANCA MUEVE DERECHA
  else if (direccion === codigosDireccion.IZQUIERDA) {
    nuevaFilaPiezaVacia = filaVacia;
    nuevaColumnaPiezaVacia = columnaVacia + 1;
  }

  /* A continuación se chequea si la nueva posición es válida, si lo es, se intercambia. 
  Para que esta parte del código funcione correctamente deberás haber implementado  las funciones posicionValida, intercambiarPosicionesGrilla y actualizarPosicionVacia */

  /* Dentro de la misma función redefine gracias al parámetro los valores de las var declaradas al principio de la misma y las pasa como parámetro para ejecutar el resto de las funciones más arriba en el código.
  Primero chequea si la posición deseada es válida; después intercambia las posiciones; por último actualiza la posición de la ficha vacía. Termina agregando el movimiento al array movimientos[] con la función declarada previamente*/

    if (posicionValida(nuevaFilaPiezaVacia, nuevaColumnaPiezaVacia)) {
        intercambiarPosiciones(filaVacia, columnaVacia, nuevaFilaPiezaVacia, nuevaColumnaPiezaVacia);
        actualizarPosicionVacia(nuevaFilaPiezaVacia, nuevaColumnaPiezaVacia);

        agregarUltMov(direccion);
        ultimos3Movimientos(movimientos);

    }
}


//////////////////////////////////////////////////////////
////////A CONTINUACIÓN FUNCIONES YA IMPLEMENTADAS.////////
/////////NO TOCAR A MENOS QUE SEPAS LO QUE HACES//////////
//////////////////////////////////////////////////////////

/* Las funciones y variables que se encuentran a continuación ya están implementadas.
No hace falta que entiendas exactamente que es lo que hacen, ya que contienen
temas aún no vistos. De todas formas, cada una de ellas tiene un comentario
para que sepas que se está haciendo a grandes rasgos. NO LAS MODIFIQUES a menos que
entiendas perfectamente lo que estás haciendo! */

/* codigosDireccion es un objeto que te permite reemplazar
el uso de números confusos en tu código. Para referirte a la dir
izquierda, en vez de usar el número 37, ahora podés usar:
codigosDireccion.IZQUIERDA. Esto facilita mucho la lectura del código. */
var codigosDireccion = {
    IZQUIERDA: 37,
    ARRIBA: 38,
    DERECHA: 39,
    ABAJO: 40
}

/* Funcion que realiza el intercambio logico (en la grilla) y ademas actualiza
el intercambio en la pantalla (DOM). Para que funcione debera estar implementada
la funcion intercambiarPosicionesGrilla() */
function intercambiarPosiciones(fila1, columna1, fila2, columna2) {
  // Intercambio posiciones en la grilla
  var pieza1 = grilla[fila1][columna1];
  var pieza2 = grilla[fila2][columna2];

  intercambiarPosicionesGrilla(fila1, columna1, fila2, columna2);
  intercambiarPosicionesDOM('pieza' + pieza1, 'pieza' + pieza2);

}

/* Intercambio de posiciones de los elementos del DOM que representan
las fichas en la pantalla */
//Aparentemente usa clones "temporales" que después usa para intercambiar sus valores

function intercambiarPosicionesDOM(idPieza1, idPieza2) {
  // Intercambio posiciones en el DOM
  var elementoPieza1 = document.getElementById(idPieza1);
  var elementoPieza2 = document.getElementById(idPieza2);

  var padre = elementoPieza1.parentNode;

  var clonElemento1 = elementoPieza1.cloneNode(true);
  var clonElemento2 = elementoPieza2.cloneNode(true);

  padre.replaceChild(clonElemento1, elementoPieza2);
  padre.replaceChild(clonElemento2, elementoPieza1);
}

/* Actualiza la representación visual del último movimiento 
en la pantalla, representado con una flecha. */
function actualizarUltimoMovimiento(direccion) {
  ultimoMov = document.getElementById('flecha');
  switch (direccion) {
    case codigosDireccion.ARRIBA:
      ultimoMov.textContent = '↑';
      break;
    case codigosDireccion.ABAJO:
      ultimoMov.textContent = '↓';
      break;
    case codigosDireccion.DERECHA:
      ultimoMov.textContent = '→';
      break;
    case codigosDireccion.IZQUIERDA:
      ultimoMov.textContent = '←';
      break;
  }
}


/* Esta función permite agregar una instrucción a la lista
con idLista. Se crea un elemento li dinámicamente con el texto 
pasado con el parámetro "instrucción". */
function mostrarInstruccionEnLista(instruccion, idLista) {
  var ul = document.getElementById(idLista);
  var li = document.createElement("li");
  li.textContent = instruccion;
  ul.appendChild(li);
}

/* Función que mezcla las piezas del tablero una cantidad de veces dada.
Se calcula una posición aleatoria y se mueve en esa dirección. De esta forma
se mezclará todo el tablero. */

function mezclarPiezas(veces) {
  if (veces <= 0) {
    return;
  }
  
  var direcciones = [codigosDireccion.ABAJO, codigosDireccion.ARRIBA,
      codigosDireccion.DERECHA, codigosDireccion.IZQUIERDA
    ];

  var direccion = direcciones[Math.floor(Math.random() * direcciones.length)];
  moverEnDireccion(direccion);

  setTimeout(function() {
      mezclarPiezas(veces - 1);
    }, 100);
}

/* capturarTeclas: Esta función captura las teclas presionadas por el usuario. Javascript
permite detectar eventos, por ejemplo, cuando una tecla es presionada y en 
base a eso hacer algo. No es necesario que entiendas como funciona esto ahora, 
en el futuro ya lo vas a aprender. Por ahora, sólo hay que entender que cuando
se toca una tecla se hace algo en respuesta, en este caso, un movimiento */
function capturarTeclas() {
  document.body.onkeydown = (function(evento) {
    if (evento.which === codigosDireccion.ABAJO ||
      evento.which === codigosDireccion.ARRIBA ||
      evento.which === codigosDireccion.DERECHA ||
      evento.which === codigosDireccion.IZQUIERDA) {

      moverEnDireccion(evento.which);

        var gano = chequearSiGano();
        if (gano) {
          setTimeout(function() {
              mostrarCartelGanador();
              }, 500);
            }
            evento.preventDefault();
        }
    })
}

/* Se inicia el rompecabezas mezclando las piezas 60 veces 
y ejecutando la función para que se capturen las teclas que 
presiona el usuario */
function iniciar() {
    mostrarInstrucciones(instrucciones);
    mezclarPiezas(20);
    setTimeout(function() {
      movimientos=[]; //Pone delay a lo que haya dentro de la funcion
      }, 3000);

    
    capturarTeclas();
}

// Ejecutamos la función iniciar
iniciar();