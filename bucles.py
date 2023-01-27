import random
num=random.randint(0,1000000)

num2=int(input("Dime un número "))
while num!=num2:
    if num<num2:
        num2=int(input("No, más pequeño "))
    if num>num2:
        num2=int(input("No, más grande "))
print("sí!!! Era el "+str(num))