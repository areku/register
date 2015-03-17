
from register import *

from unittest import *

class BaseTest(TestCase):
    def test_register(self):
        # create registry
        r = Registry()


        @r
        def abc():
            pass

        @r(a = 2, b = 3)
        def de():
            pass

        @r("test")
        def a(): pass


        self.assertTrue( "abc" in r)
        self.assertTrue( "de" in r)
        self.assertTrue( "test" in r)

        self.assertIs(abc, r.lookup("abc"))
        self.assertIs(de, r.lookup("de"))
        self.assertIs(a, r.lookup("test"))

        self.assertDictEqual(dict(a=2,b=3), r.meta("de"))

    def test_class_register(self):
        r = Registry()
        @r
        class A(object): pass

        @r("B")
        class A(object): pass

        self.assertTrue( "A" in r)
        self.assertTrue( "B" in r)

        self.assertIs(A, r.lookup("B"))
        self.assertIsNot(A, r.lookup("A"))


if __name__ == '__main__':
    main()