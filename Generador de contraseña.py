import random #se encarga como dice su nombre dar aleatoriedad
Usuario=input("ingrese su Usuario o Nombre")
longitud=int(input("Ingrese el tamaño de su contraseña")) 
#super importante definir como entero, como string no permite usar el while
contador= 0
contrasena=""
abecedario="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$%&/?¡"
while contador<longitud: #a diferencia de raptor aqui hay que ir por la ruta del NO
    #random.choice funcion de python que permite la aleatoriedad
    caracter_random=random.choice(abecedario) #random elije un caracter de abecedario
    contrasena= contrasena + caracter_random
    contador= contador+1
print("Usuario:"+ Usuario + " Tu contraseña generada es:"+ contrasena)
if longitud<8:
    #En raptor lenghtof mide la longitud de las opciones, random genera la aleatoriedad y floor evita los decimales 
    
    print("Seguridad: Debil se recomienda como minimo 8 caracteres por su seguridad")
else:
    print("Seguridad: FUERTE se cumple con todos los requisitos previos para su seguridad")
   #a diferencia de python que empieza en 0 en raptor +1 permite que el codigo empiece en esa posicion
   