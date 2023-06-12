#Realice un programa que cambie pesos a dólares. Méjorelo, añadiendo el cambio de dólares a pesos y que sea el usario quién decida que tipo de cambio quiere, si de dólares a pesos o viceversa.

tipo_cambio = float(input("Ingrese el tipo de cambio: ")) #1 dólar equivale a 244,76 pesos
cantidad = float(input("Ingrese la cantidad a convertir: "))
opcion = input("Seleccione una opción (1: Dólares a pesos, 2: Pesos a dólares): ")

if opcion == "1":
    conversion = cantidad * tipo_cambio
    print(f"{cantidad} dólares equivale a {conversion} pesos") #f-string https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
if opcion == "2":
    conversion = cantidad / tipo_cambio
    print(f"{cantidad} pesos equivale a {conversion} dólares")

print("Fin del programa")