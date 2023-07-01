#Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.

def suma(a,b,c):
    resultado = a + b + c
    return resultado

for i in range(2):
    print(suma(int(input("Ingrese el primer número: ")),
               int(input("Ingrese el segundo número: ")),
               int(input("Ingrese el tercer número: "))))

print("Fin del programa")