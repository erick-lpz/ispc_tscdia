#Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen), ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. 

def mensaje(aula,mensaje):
    print("\nHola Aula",aula,",¿Qué tal?")
    print(mensaje)
    print("")

for i in range(3):    
    mensaje(int(input("Ingrese el número de aula: ")),(input("Ingrese un mensaje: ")))

print("Fin del programa")