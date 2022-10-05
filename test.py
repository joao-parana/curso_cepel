import unittest
from cepel import cepel

class MyTest(unittest.TestCase):
    def test(self):
        print('testando')
        self.assertEqual(cepel.soma(1, 2), 4)

if __name__ == '__main__':
    unittest.main()
