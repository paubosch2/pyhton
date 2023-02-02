import random

op=[0,1,2,3,4,5,6,7,8]
casilla=[" "," "," "," "," "," "," "," "," "]
seguir=True
tie=9

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
    if pos in op:
        casilla[pos]="X"
        op.remove(pos)
    else:
        print("Ya está ocupado")
        pos=int(input("Elige una casilla del 0 al 8 "))
        casilla[pos]="X"
        op.remove(pos)
    
    

    if casilla[0] == casilla[1] == casilla[2] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break 
    

    if casilla[3] == casilla[4] == casilla[5] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break
   

    if casilla[6] == casilla[7] == casilla[8] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break
   

    if casilla[0] == casilla[3] == casilla[6] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break
 

    if casilla[1] == casilla[4] == casilla[7] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break


    if casilla[2] == casilla[5] == casilla[8] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break

    if casilla[0] == casilla[4] == casilla[8] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break


    if casilla[2] == casilla[4] == casilla[6] == "X":
        print("Ganaste a un bot, Orgulloso?")
        seguir=False
        break


    tie=tie-1
    if tie==0:
        seguir=False
        print("Empate!!!")
        break

    
    pc=random.choice(op)
    casilla[pc]="O"
    op.remove(pc)

 
    if casilla[0] == casilla[1] == casilla[2] == "O":
        print("Perdiste jajaja")
        seguir=False
        break


    if casilla[3] == casilla[4] == casilla[5] == "O":
        print("Perdiste jajaja")
        seguir=False
        break

    if casilla[6] == casilla[7] == casilla[8] == "O":
        print("Perdiste jajaja")
        seguir=False
        break

 
    if casilla[0] == casilla[3] == casilla[6] == "O":
        print("Perdiste jajaja")
        seguir=False
        break

   
    if casilla[1] == casilla[4] == casilla[7] == "O":
        print("Perdiste jajaja")
        seguir=False
        break

 
    if casilla[2] == casilla[5] == casilla[8] == "O":
        print("Perdiste jajaja")
        seguir=False
        break

 
    if casilla[0] == casilla[4] == casilla[8] == "O":
        print("Perdiste jajaja")
        seguir=False
        break

 
    if casilla[2] == casilla[4] == casilla[6] == "O":
        print("Perdiste jajaja")
        seguir=False
        break
    
    tie=tie-1
    if tie==0:
        seguir=False
        print("Empate!!!")
        break







print("|"+casilla[0]+"|"+casilla[1]+"|"+casilla[2]+"|")
print("|"+casilla[3]+"|"+casilla[4]+"|"+casilla[5]+"|")
print("|"+casilla[6]+"|"+casilla[7]+"|"+casilla[8]+"|")