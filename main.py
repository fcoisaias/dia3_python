#Al principio debe mostrarle al usuario el último número de tu Nómina 
#seguido por tus iniciales
basic.show_string("6FIGC")

# Al presionar el botón A, se debe de mostrar una flecha hacia la izquierda 
# e imprima la letra "A"
def on_button_pressed_a():
    basic.show_arrow(ArrowNames.WEST)
    print("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

#Al presionar el botón B, se debe de mostrar una flecha hacia la derecha 
#e imprima la letra "B"
def on_button_pressed_a2():
    basic.show_arrow(ArrowNames.EAST)
    print("B")
input.on_button_pressed(Button.B, on_button_pressed_a2)

#Al presionarse los dos botones, se muestra una flecha hacia arriba 
#e imprima las letras "AB"
def on_button_pressed_a3():
    basic.show_arrow(ArrowNames.NORTH)
    print("AB")
input.on_button_pressed(Button.AB, on_button_pressed_a3)

#Al agitarse el Micro:Bit se muestra una cara confundida, 
#"se espera medio segundo y se borra la pantalla. 
#Seguido de esto, imprime la palabra " Shake
def on_gesture_shake():
    basic.show_icon(IconNames.CONFUSED)
    basic.pause(500)
    basic.clear_screen()
    print("Shake")
input.on_gesture(Gesture.Shake, on_gesture_shake)

#Siempre se está imprimiendo el valor de la temperatura en F
def on_forever():
    c=input.temperature()
    f=(c*9/5) + 32
    print("Grados Farenheit")
    print(f)
    if f>90:
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)

forever(on_forever)