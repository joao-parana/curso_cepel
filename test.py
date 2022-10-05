import unittest
from cepel import cepel

class MyTest(unittest.TestCase):
    def test(self):
        print('testando a classe MyTest agora com hook pre-commit local')
        print('fase 3')
        self.assertEqual(cepel.soma(1, 2), 4)

if __name__ == '__main__':
    unittest.main()

