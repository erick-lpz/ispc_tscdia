#Confeccione un programa que pida un número del 1 al 7 y diga el dia de la semana correspondiente.

num = int(input("Ingrese un número del 1 al 7: "))
if num == 1:
    print("El día de la semana es Lunes")
elif num == 2:
    print("El día de la semana es Martes")
elif num == 3:
    print("El día de la semana es Miércoles")
elif num == 4:
    print("El día de la semana es Jueves")
elif num == 5:
    print("El día de la semana es Viernes")
elif num == 6:
    print("El día de la semana es Sábado")
elif num == 7:
    print("El día de la semana es Domingo")
else:
    print("El número ingresado es incorrecto")

print("Fin del programa")