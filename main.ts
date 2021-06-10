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
// Al agitarse el Micro:Bit se muestra una cara confundida, 
// "se espera medio segundo y se borra la pantalla. 
// Seguido de esto, imprime la palabra " Shake
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Confused)
    basic.pause(500)
    basic.clearScreen()
    console.log("Shake")
})
// Siempre se está imprimiendo el valor de la temperatura en F
forever(function on_forever() {
    let c = input.temperature()
    let f = c * 9 / 5 + 32
    console.log("Grados Farenheit")
    console.log(f)
})
