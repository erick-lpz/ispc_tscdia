#Realice un programa que lea tres números, muestre cúal es el mayor y determine si es par o impar.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print("El número mayor es:", mayor)

if mayor % 2 == 0:
    print("El número mayor es par")
else:
    print("El número mayor es impar")

print("Fin del programa")