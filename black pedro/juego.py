from baraja import Baraja
from mano import Mano


mibaraja=Baraja()
mano1=Mano()
bot=Mano()

mibaraja.mezclar()

#mibaraja.mostrar() 

cartacogida=mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
cartacogida=mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)

mano1.mostrar_mano()

mano1.calcula_valor()
print(mano1.valor)
while True:
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

while True: 
    if Vida > 21:
        break
    if Vida == 21:
        break
    cartacogida=mibaraja.coger_carta()
    bot.añadir_carta(cartacogida)
    cartacogida=mibaraja.coger_carta()
    bot.añadir_carta(cartacogida)
    if bot.valor < mano1.valor:
        
        cartacogida=mibaraja.coger_carta()
        bot.añadir_carta(cartacogida)
    if bot.valor > mano1.valor > 22:
        print("el bot ha ganado xd")
        break
    if bot.valor > 21:
        print("Has ganado")
        break
    if bot.valor == 21:
            print("BlackPedro para el bot. ibècil.")
            break


        

print("Fin del juego")
print(mano1.valor)
print("bot "+str(bot.valor))



