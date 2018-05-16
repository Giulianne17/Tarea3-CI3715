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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()