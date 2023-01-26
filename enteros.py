import math

a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
disc = int(((b**2)-(4*a*c)))

if disc > 0 :
    print("La equación tiene 2 soluciones")
    print((-b*+math.sqrt(b**2-(4*a*c))/(2*a)))
    print((-b*-math.sqrt(b**2-(4*a*c))/(2*a)))

if disc == 0 :
    print("La equación tiene 1 solución")
    print((-b*+math.sqrt(b**2-(4*a*c))/(2*a)))

if disc < 0 :
    print("ta mal, no tiene solución")



print((-b*+math.sqrt(b**2-(4*a*c))/(2*a)))
print((-b*-math.sqrt(b**2-(4*a*c))/(2*a)))

