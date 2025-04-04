// Crear una función JS que acepte 4 argumentos. 
// Sumar los dos primeros argumentos, luego los dos segundos y multiplicarlos. 
// Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". 
// Si es más pequeño, la consola registra "¡El número es menor que 50!"

function calcularNumero(a, b, c, d) {
    let suma1 = a + b;
    let suma2 = c + d;
    let resultado = suma1 * suma2;

    if (resultado > 50) {
        console.log("¡El número es mayor que 50!");
    } else {
        console.log("¡El número es menor que 50!");
    }
}

calcularNumero(7, 10, 3, 6); 