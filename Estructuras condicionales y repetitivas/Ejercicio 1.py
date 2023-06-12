#Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

contador_pares = 0
sumatoria_pares = 0

for i in range(4):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        contador_pares += 1
        sumatoria_pares += num

contador_impares = 4 - contador_pares

print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)
print("Sumatoria de los números pares:", sumatoria_pares)