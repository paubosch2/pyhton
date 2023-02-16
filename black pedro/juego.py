from baraja import Baraja
from mano import Mano

mibaraja=Baraja()
mano1=Mano()

mibaraja.mezclar()

#mibaraja.mostrar() 

cartacogida=mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
cartacogida=mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)

mano1.mostrar_mano()

mano1.calcula_valor()
print(mano1.valor)
seguir=True
while seguir:
    Vida=mano1.valor
    if Vida > 21:
        print("Has perdido")
        break
    if Vida == 21:
        print("BlackPedro")
        break
    juego=input("Quieres seguir? S/N ")
    if juego == "N":
        break
    if juego == "S":
        cartacogida=mibaraja.coger_carta()
        mano1.añadir_carta(cartacogida)
        mano1.mostrar_mano()
        mano1.calcula_valor()
        print(mano1.valor)

        

print("Fin del juego")
print(mano1.valor)



