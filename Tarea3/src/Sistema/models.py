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
        except:
            if (clave1 != clave2):
                return 0
            