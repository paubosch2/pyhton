import random

while True:
    piedra

    op=["piedra","papel","tijera"]

    pc=random.choice(op)
    usuario=input("Piedra Pepel o Tijera saca lo que quieras 1,2,3, ya! ")

    if  pc==usuario:
        print("Empate!!")

    if usuario=="piedra" and pc=="tijera":
        print("El bot ha elegido tijera")
        print("GG! ganaste al puto bot!")
    if usuario=="papel" and pc=="tijera":
        print("El bot ha elegido tijera")
        print("Jajajaj! Malisimo, perdiste!")

    if usuario=="papel" and pc=="piedra":
        print("El bot ha elegido piedra")
        print("GG! ganaste al puto bot!")
    if usuario=="tijera" and pc=="piedra":
        print("El bot ha elegido piedra")
        print("Jajajaj! Malisimo, perdiste!")

    if usuario=="tijera" and pc=="papel":
        print("El bot ha elegido papel")
        print("GG! ganaste al puto bot!")
    if usuario=="piedra" and pc=="papel":
        print("El bot ha elegido papel")
        print("Jajajaj! Malisimo, perdiste!")