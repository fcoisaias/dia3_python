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

