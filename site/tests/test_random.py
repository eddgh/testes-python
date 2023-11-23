import sys
sys.path.append(".")
from utils import *

class TestsRandom:
    def test_one(self):
        a = 1 + 1
        assert a == 2
        print('Resultado de a (1+1) = ', a)

    def test_two(self):
        a = 2 * 4
        assert a == 8
        print('Resultado de a (2 x 4) = ', a)               
    
    def test_three(self):
        a = soma(4, 4)
        assert a == 8      
        print('resultado de a = ', a)  