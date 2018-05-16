from django.db import models

import django
import re

class Seguridad:
    def registrarUsuario(self, correo, clave1, clave2):
        try:
            assert(re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$",correo,flags=0)!=None)
            pass
        except :
            print("Correo electrónico inválido")
            exit()
        try:
            assert(clave1==clave2)
            
            # Su longitud debe estar entre 8 y 16 caracteres
            assert(8<=len(clave1)<=16)
            
                        
            # Su longitud debe estar entre 8 y 16 caracteres
            assert(8<=len(clave1)<=16)

            # No debe incluir caracteres especiales.
            assert((clave1.isalnum()!=False))
            
            #Al menos tres letras y al menos una de ellas debe ser mayúscula y una minúscula
            #Debe contener al menos un dígito.
            digito1 = 0
            totalLetras1 = 0
            cantidadMayusculas1=0
            cantidadMinusculas1=0
            for i in range(len(clave1)):
                if (clave1[i].isdigit()):
                    digito1+=1
                elif (clave1[i].isupper()):
                    cantidadMayusculas1 +=1
                elif (clave1[i].islower()):
                    cantidadMinusculas1 +=1
            
            totalLetras1=cantidadMayusculas1+cantidadMinusculas1
            
            #Revisando minimo de letras, de mayusculas, de minusculas y de digitos

            assert(totalLetras1 >= 3)
            assert(cantidadMayusculas1!=0 and cantidadMinusculas1!=0)
            assert(digito1 >= 1)

            return 7
            
        except:
            if (clave1 != clave2):
                return 0
            elif (8>len(clave1) or len(clave1)>16):
                return 1
            elif (clave1.isalnum()==False):
                return 2
            elif (totalLetras1<3):
                return 3
            elif (cantidadMayusculas1 == 0):
                return 4
            elif (cantidadMinusculas1 == 0):
                return 5
            elif (digito1==0):  
                return 6
        