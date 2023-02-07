trys=6

palabra="antifaz"
resolver=[]
fallos=[]


durada=len(palabra)


while durada>0:
    print("_ ", end=" ")
    durada=durada-1
l=input("dime letra ")

for letra in palabra:
    if letra in resolver:
        print(letra,ens="")
    else:
        print("_ ",end="")














'''
l=input("dime letra ")
print(resolver)
print(fallos)
if letra==l:
    resolver,append(letra)
else:
    fallos.append(letra)

for letra in palabra:
    if letra in resolver:
        print(resolver, end="")
        
else:
    print("_ ",end="")

print("correctas ", )