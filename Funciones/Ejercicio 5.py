#Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente. Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta(a,b):
    suma = a + b
    resta = a - b
    print("La suma de",a,"y",b,"es:",suma)
    print("La resta de",a,"y",b,"es:",resta)

sumayresta(int(input("Ingrese el primer número: ")),
           int(input("Ingrese el segundo número: ")))

print("Fin del programa")