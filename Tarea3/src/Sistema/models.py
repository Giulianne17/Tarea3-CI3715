from django.db import models

import django
import re

class Seguridad:
    
    usuarioClave={}
    
    def registrarUsuario(self, correo, clave1, clave2):
        try:
            assert(re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$",correo,flags=0)!=None)
            pass
        except :
            print("Correo electrónico inválido")
            return 8
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
            
            claveReversa= clave1[::-1]

            usuarioClave[correo]=claveReversa
            
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
    
    def ingresarUsuario(self, correo, clave1):
        ###Inicio validaciones
        try:
            assert(re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$",correo,flags=0)!=None)
            pass
        except :
            print("Correo electrónico inválido")
            return 8
    
        try:

            # Su longitud debe estar entre 8 y 16 caracteres
            assert(8<=len(clave1)<=16)
            
            #No debe incluir caracteres especiales.
            assert((clave1.isalnum()!=False))
            
            #Al menos tres letras y al menos una de ellas debe ser mayúscula y una minúscula
            #Debe contener al menos un dígito.
            digito1 = 0
            cantidadMayusculas1=0
            cantidadMinusculas1=0
            for i in range(len(clave1)):
                if (clave1[i].isdigit()):
                    digito1=1
                elif (clave1[i].isupper()):
                    cantidadMayusculas1 +=1
                elif (clave1[i].islower()):
                    cantidadMinusculas1 +=1
            
            totalLetras1=cantidadMayusculas1+cantidadMinusculas1
            
            #Chequeando
            assert(totalLetras1>=3)
            assert(cantidadMayusculas1!=0 and cantidadMinusculas1!=0)
            assert(digito1==1)
            
            return 7
            
        except:
            print("Clave inválida")
            if (8>len(clave1) or len(clave1)>16):
                print("Las claves deben tener una longitud entre 8 y 16 caracteres")
            elif (clave1.isalnum()==False):
                print("Las claves deben ser alfanumericas")
            elif (totalLetras1<3):
                print("Las claves deben tener al menos tres letras")
            elif (cantidadMayusculas1==0):
                print("Las claves deben tener al menos una mayuscula")
            elif (cantidadMinusculas1==0):
                print("Las claves deben tener al menos una minuscula")
            elif (digito1==0):
                print("Las claves deben tener al menos un digito")  
        ###Fin Validaciones
        
        try:
            assert(correo in self.usuarioClave)
        
        except:
            print("Usuario inválido.")
            return 8

        try:
            claveReversa=clave[::-1]
            assert(self.usuarioClave[correo]==claveReversa)
            
        except:
            print("Clave inválida.")
            return 9

        print("Usuario aceptado.")
        return 7
