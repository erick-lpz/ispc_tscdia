#Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo "puede votrar", sino "no vota".

edad = int(input("Ingrese su edad: "))

if edad >= 16:
    print("Puede votar")
if edad < 16:
    print("No puede votar")

print("Fin del programa")