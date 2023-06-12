#Realice un programa que permita al usuario simular el pago ingresando el importe y forma de pago:
#Contacto(1): se aplica un descuento del 10% al importe.
#Tarjeta(2): se aplica un interés del 10%.
#Débito(3): se aplica un descuento del 5%.
#Mostrar el importe, el descuento o interés y el importe total.

importe = float(input("Ingrese el importe: "))
formaDePago = int(input("Ingrese la forma de pago: \n1.Contado\n2.Tarjeta\n3.Débito\n"))
print("El importe es: ",importe)

if formaDePago == 1:
    importe_contacto = importe * 0.1 #10% del importe
    importe = importe - importe_contacto
    print("El importe del descuento es: ",importe_contacto)
elif formaDePago == 2:
    importe_tarjeta = importe * 0.1 #10% del importe
    importe = importe + importe_tarjeta
    print("El importe del interés es: ",importe_tarjeta)
elif formaDePago == 3:
    importe_debito = importe * 0.05 #5% del importe
    importe = importe - importe_debito
    print("El importe del descuento es: ",importe_debito) 
else:
    print("La forma de pago ingresada es incorrecta")

print("El importe total a pagar es: ",importe)
print("Fin del programa")