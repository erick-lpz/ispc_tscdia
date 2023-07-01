#Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE.

def comparar(a,b):
    if a == b:
        return True
    else:
        return False

print(comparar(int(input("Ingrese el primer número: ")),
               int(input("Ingrese el segundo número: "))))

print("Fin del programa")