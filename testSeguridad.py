import unittest
from Sistema.migrations import models 

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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()