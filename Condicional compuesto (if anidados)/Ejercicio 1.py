#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero") #Equilátero: Los tres lados son iguales.
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: 
    print("El triángulo es isósceles") #Isósceles: Dos lados son iguales y el otro mide distinto.
else:
    print("El triángulo es escaleno")  #Escaleno: Los tres lados son diferentes.

print("Fin del programa")