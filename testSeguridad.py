import unittest
from Seguridad import *

class Test(unittest.TestCase):

	def setUp(self):
		self.Seguridad = Seguridad()
		pass

	def tearDown(self):
		self.Seguridad = None
		pass

	#Caso de prueba para cuando las claves ingresadas son distintas
	def test_ClavesDistintas(self):
		self.correo = "correoejemplo@usb.ve"
		self.clave1 = "Abc15246"
		self.clave2 = "Abc15245"
		self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 0, "Las claves ingresadas son distintas")

	# Caso de prueba para cuando la clave ingresada posee menos de 8 caracteres
	def test_ClaveCorta(self):
		self.correo = "correoejemplo@usb.ve"
		self.clave1 = "Abc1"
		self.clave2 = "Abc1"
		self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 1, "La clave ingresada es muy corta")

	# Caso de prueba para cuando la clave ingresada posee mas de 16 caracteres
	def test_ClaveLarga(self):
		self.correo = "correoejemplo@usb.ve"
		self.clave1 = "Abc123456789111abc"
		self.clave2 = "Abc123456789111abc"
		self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 1, "La clave ingresada es muy larga")

	# Caso de prueba para cuando la clave ingresada posee caracteres especiales
	def test_Alfanumerico(self):
		self.correo = "correoejemplo@usb.ve"
		self.clave1 = "Abc-123456789111"
		self.clave2 = "Abc-123456789111"
		self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 2, "La clave ingresada contiene caracteres especiales")

	# Caso de prueba para cuando la clave no cuenta con la cantidad minima de letras
	def test_minLetras(self):
		self.correo = "correoejemplo@usb.ve"
		self.clave1 = "Ab123456789"
		self.clave2 = "Ab123456789"
		self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 3, "La clave ingresada contiene menos de tres letras")

	# Caso de prueba para cuando la clave no posee ninguna letra mayuscula
	def test_minMayus(self):
		self.correo = "correoejemplo@usb.ve"
		self.clave1 = "abc123456789"
		self.clave2 = "abc123456789"
		self.assertTrue(self.Seguridad.registrarUsuario(self.correo, self.clave1, self.clave2) == 4, "La clave ingresada no posee ninguna letra mayuscula")
	
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()