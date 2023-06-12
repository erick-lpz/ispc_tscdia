#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

contador_mayores = 0
contador_menores = 0
numero_maximo = 0
numero_minimo = float("inf") #Inicializamos el número mínimo con un valor muy grande

for i in range(10):
    numero = float(input("Ingrese un número: "))
    
    if numero > 100:
        contador_mayores += 1
    elif numero < 100:
        contador_menores += 1
    
    if numero > numero_maximo:
        numero_maximo = numero
    
    if numero < numero_minimo:
        numero_minimo = numero

print("Cantidad de números mayores a 100:", contador_mayores)
print("Cantidad de números menores a 100:", contador_menores)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)
print("Fin del programa")