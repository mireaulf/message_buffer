import unittest
from package import package

class package_test(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            package(None)
        with self.assertRaises(TypeError):
            package(42)
        stream = 'Hello world!'    
        pkg = package(stream)
        self.assertEqual(stream, pkg.stream)

if __name__ == '__main__':
    unittest.main()
