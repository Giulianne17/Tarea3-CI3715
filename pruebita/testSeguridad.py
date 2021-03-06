import unittest
from sistema.models import Seguridad

class Test(unittest.TestCase):

    def setUp(self):
        self.Seguridad = Seguridad()
        pass

    def tearDown(self):
        self.Seguridad = None
        pass

    #Caso de prueba para cuando las claves ingresadas son distintas. Malicioso
    def test_ClavesDistintas(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Abc15246"
        self.clave2 = "Abc15245"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 0, "Las claves ingresadas son distintas")

    # Caso de prueba para cuando la clave ingresada posee menos de 8 caracteres. Esquina
    def test_ClaveCorta(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Abc1"
        self.clave2 = "Abc1"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 1, "La clave ingresada es muy corta")

    # Caso de prueba para cuando la clave ingresada posee mas de 16 caracteres. Esquina
    def test_ClaveLarga(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Abc123456789111abc"
        self.clave2 = "Abc123456789111abc"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 1, "La clave ingresada es muy larga")

    # Caso de prueba para cuando la clave ingresada posee caracteres especiales. Malicioso
    def test_Alfanumerico(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Abc-123456789111"
        self.clave2 = "Abc-123456789111"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 2, "La clave ingresada contiene caracteres especiales")

    # Caso de prueba para cuando la clave no cuenta con la cantidad minima de letras. Esquina
    def test_minLetras(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Ab123456789"
        self.clave2 = "Ab123456789"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 3, "La clave ingresada contiene menos de tres letras")

    # Caso de prueba para cuando la clave no posee ninguna letra mayuscula. Malicioso
    def test_minMayus(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "abc123456789"
        self.clave2 = "abc123456789"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 4, "La clave ingresada no posee ninguna letra mayuscula")

    # Caso de prueba para cuando la clave no posee ninguna letra minuscula. Malicioso
    def test_minMinus(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "ABC123456789"
        self.clave2 = "ABC123456789"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 5, "La clave ingresada no posee ninguna letra minuscula")

    # Caso de prueba para cuando la clave no posee ningun digito. Malicioso
    def test_minDigito(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "AaBbCcDd"
        self.clave2 = "AaBbCcDd"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 6, "La clave ingresada no posee ningun digito")

    # Caso de prueba para cuando la clave posee el minimo de digitos, Frontera
    def test_exactoDigito(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "AaBbCcDd1"
        self.clave2 = "AaBbCcDd1"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 7)

    # Caso de prueba para cuando la clave posee el minimo de letras minusculas. Frontera
    def test_exactoMinus(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "ABCa12345"
        self.clave2 = "ABCa12345"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 7)

    # Caso de prueba para cuando la clave posee el minimo de letras mayusculas. Frontera
    def test_exactoMayus(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aabcd12345"
        self.clave2 = "Aabcd12345"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 7)

    # Caso de prueba para cuando la clave posee el minimo de caracteres permitido. Frontera
    def test_exactoMin(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345"
        self.clave2 = "Aab12345"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 7)

    # Caso de prueba para cuando la clave posee el maximo de caracteres permitido. Frontera
    def test_exactoMax(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 7)
    
    # Cso en el que el correo no cuenta con ningun @. Malicioso
    def test_correoSinArroba(self):
        self.correo = "correoejemplousb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 8)
    
    # Caso en el que el correo posee muchos puntos despues del arroba. Dentro del dominio
    def test_correoMulPunto(self):
        self.correo = "correoejemplo@usb.v.e"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 7)
    
    #Caso de prueba para ver si registra el correo. Dentro del dominio
    def test_registroCorreoUsuario(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.x = self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2)
        self.assertTrue(self.correo in self.Seguridad.usuarioClave)
    
    #Caso de prueba para ver si se guarda la clave codificada. Dentro del dominio
    def test_registroClaveUsuario(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.x = self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2)
        print(self.correo)
        self.claveReversa = self.clave1[::-1] 
        self.assertTrue(self.Seguridad.usuarioClave[self.correo]==self.claveReversa)
        
    #Casos de prueba para ingresar un usuario. Malicioso
    def test_ingresarCorreoMalo(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.x = self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2)
        self.assertTrue(self.Seguridad.ingresarUsuario("correoejemp@usb.ve",self.clave1)==9)
    
    #Casos de prueba para ingresar un usuario con clave incorrecta. Malicioso
    def test_ingresarClaveMala(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.x = self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2)
        self.assertTrue(self.Seguridad.ingresarUsuario(self.correo,"Aab12345aaaaaaab")==10)
        
    #Casos de prueba para ingresar un usuario correcto. Dentro del domino
    def test_ingresarUsuarioCorrecto(self):
        self.correo = "correoejemplo@usb.ve"
        self.clave1 = "Aab12345aaaaaaaa"
        self.clave2 = "Aab12345aaaaaaaa"
        self.x = self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2)
        self.assertTrue(self.Seguridad.ingresarUsuario(self.correo,self.clave1)==7)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()