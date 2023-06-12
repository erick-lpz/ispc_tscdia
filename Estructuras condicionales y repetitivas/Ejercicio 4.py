#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

contador_positivos = 0
sumatoria_positivos = 0

for i in range(10):
    numero = float(input("Ingrese un número: "))
    if numero > 0:
        contador_positivos += 1
        sumatoria_positivos += numero

print("Cantidad de números positivos:", contador_positivos)
print("Sumatoria de los números positivos:", sumatoria_positivos)
print("Fin del programa")