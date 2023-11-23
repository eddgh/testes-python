import sys
sys.path.append(".")
from utils import *

class TestVariables:
    def test_variables_one(self):                
        print(nome) 
        assert nome == 'Edmundo'
        
        print(telefone) 
        assert telefone == '995322704'
        
        resultado = soma(2, 4)
        assert resultado == 6
        print(resultado)
        
    def test_variables_two(self):
        a = 1 + 1
        assert a == 2
        print('Resultado de a (1+1) = ', a)

    