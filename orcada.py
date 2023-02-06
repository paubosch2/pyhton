trys=6

palabra="antifaz"
resolver=[]
fallos=[]


durada=len(palabra)


while durada>0:
    print("_ ", end=" ")
    durada=durada-1

while True:
    l=input("dime letra ")
    for letra in palabra:
        if letra == l:
            print(letra, end="")
            resolver.append(letra)
    else:
        print("_ ",end="")
        fallos.append(letra)
    print(fallos)
