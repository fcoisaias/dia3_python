// Al principio debe mostrarle al usuario el último número de tu Nómina 
// seguido por tus iniciales
basic.showString("6FIGC")
//  Al presionar el botón A, se debe de mostrar una flecha hacia la izquierda 
//  e imprima la letra "A"
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showArrow(ArrowNames.West)
    console.log("A")
})
// Al presionar el botón B, se debe de mostrar una flecha hacia la derecha 
// e imprima la letra "B"
input.onButtonPressed(Button.B, function on_button_pressed_a2() {
    basic.showArrow(ArrowNames.East)
    console.log("B")
})
// Al presionarse los dos botones, se muestra una flecha hacia arriba 
// e imprima las letras "AB"
input.onButtonPressed(Button.AB, function on_button_pressed_a3() {
    basic.showArrow(ArrowNames.North)
    console.log("AB")
})
