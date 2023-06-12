#Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

mes = int(input("Ingrese un número del 1 al 12: "))
if mes == 1:
    print("El mes es Enero")
elif mes == 2:
    print("El mes es Febrero")
elif mes == 3:
    print("El mes es Marzo")
elif mes == 4:
    print("El mes es Abril")
elif mes == 5:
    print("El mes es Mayo")
elif mes == 6:
    print("El mes es Junio")
elif mes == 7:
    print("El mes es Julio")
elif mes == 8:
    print("El mes es Agosto")
elif mes == 9:
    print("El mes es Septiembre")
elif mes == 10:
    print("El mes es Octubre")
elif mes == 11:
    print("El mes es Noviembre")
elif mes == 12:
    print("El mes es Diciembre")
else:
    print("El número ingresado es incorrecto")

print("Fin del programa")