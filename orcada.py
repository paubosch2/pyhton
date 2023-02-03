trys=6

palabra="antifaz"
resolver=[]


durada=len(palabra)


while durada:
    print("_ ", end=" ")
    durada=durada-1
l=input("dime letra ")
for letra in palabra:
    if letra == l:
        resolver.append(letra)
        print(resolver)
    else:
        print("_",end="")