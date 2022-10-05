import unittest
from cepel import cepel

class MyTest(unittest.TestCase):
    def test(self):
        print('testando a classe MyTest agora com hook pre-commit local')
        self.assertEqual(cepel.soma(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
