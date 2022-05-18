import unittest

from progs_teste import soma,testanumeros,carrosgaragem

class TestProg(unittest.TestCase):
    
    # 1 Teste
    
    def test_soma(self):
        self.assertEqual(soma(2,3),5)
    
    
    # 2 Teste    
    
    def test_numeros(self):
        self.assertEqual(testanumeros(2,2),"OK Numeros Maiores")
        
    
    # 3 Teste
    
    def test_carrosnagaragem(self):
        self.assertTrue(carrosgaragem("Fusca"))
        
        
    
    


unittest.main(verbosity=2)