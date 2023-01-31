import random

op=[0,1,2,3,4,5,6,7,8]
casilla=[" "," "," "," "," "," "," "," "," "]
seguir=True

'''
|0|1|2|
|3|4|5|
|6|7|8|
'''
while seguir:
    print("|"+casilla[0]+"|"+casilla[1]+"|"+casilla[2]+"|")
    print("|"+casilla[3]+"|"+casilla[4]+"|"+casilla[5]+"|")
    print("|"+casilla[6]+"|"+casilla[7]+"|"+casilla[8]+"|")
    pos=int(input("Elige una casilla del 0 al 8 "))
    casilla[pos]="X"

    pc=random.choice(op)
    if casilla[pc] == "X" == "O":
        pc=random.choice(op)
    else:
        casilla[pc]="O"

    if casilla[0] == casilla[1] == casilla[2] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[0] == casilla[1] == casilla[2] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[3] == casilla[4] == casilla[5] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[3] == casilla[4] == casilla[5] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[6] == casilla[7] == casilla[8] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[6] == casilla[7] == casilla[8] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[0] == casilla[3] == casilla[6] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[0] == casilla[3] == casilla[6] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[1] == casilla[4] == casilla[7] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[1] == casilla[4] == casilla[7] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[2] == casilla[5] == casilla[8] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[2] == casilla[5] == casilla[8] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[0] == casilla[4] == casilla[8] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[0] == casilla[4] == casilla[8] == "O":
        print("Perdiste jajaja")
        seguir=False

    if casilla[2] == casilla[4] == casilla[6] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
    if casilla[2] == casilla[4] == casilla[6] == "O":
        print("Perdiste jajaja")
        seguir=False



print("|"+casilla[0]+"|"+casilla[1]+"|"+casilla[2]+"|")
print("|"+casilla[3]+"|"+casilla[4]+"|"+casilla[5]+"|")
print("|"+casilla[6]+"|"+casilla[7]+"|"+casilla[8]+"|")