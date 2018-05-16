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
            # Las dos claves ingresadas deben ser iguales
            assert(clave1==clave2)
            
            # Su longitud debe estar entre 8 y 16 caracteres
            assert(8<=len(clave1)<=16)

            # No debe incluir caracteres especiales.
            assert((clave1.isalnum()!=False))
            
        except:
            if (clave1 != clave2):
                return 0
            elif (8>len(clave1) or len(clave1)>16):
                return 1
            elif (clave1.isalnum()==False):
                return 2