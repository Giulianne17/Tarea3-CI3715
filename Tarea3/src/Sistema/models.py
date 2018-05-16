from django.db import models

import django
import re

class Seguridad:
    def registrarUsuario(self, correo, clave1, clave2):
        
        try:
            assert(clave1==clave2)
        except:
            if (clave1 != clave2):
                return 0
            