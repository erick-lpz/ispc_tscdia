#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

numeros_positivos = [] #Creamos una lista vacía para almacenar los números positivos
 
for i in range(5):
    numero = float(input("Ingrese un número negativo: "))
    numero_positivo = numero * -1  #Multiplicamos por -1 para obtener el número positivo
    
    numeros_positivos.append(numero_positivo) #Agregamos el número positivo a la lista con append()

print("Números negativos convertidos a positivos:")
for numero in numeros_positivos: 
    print(numero)

print("Fin del programa")