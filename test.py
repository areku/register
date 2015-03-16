
from register import *



def test_a():
    r = FunctionRegister()

    @r
    def abc():
        pass


    @r(a = 2, b = 3)
    def de():
        pass

    @r("test")
    def a(): pass

    print r._register
