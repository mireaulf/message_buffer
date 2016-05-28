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
    def test_parse(self):
        stream = 'hello World!'
        pkg = package(stream)
        res = pkg.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        stream = 'this package first_package;'
        pkg = package(stream)
        res = pkg.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        stream = ' package first_package; asd '
        pkg = package(stream)
        res = pkg.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        pkg = package(stream.strip())
        res = pkg.parse()
        self.assertEqual(True, res[0])
        self.assertEqual(' asd', res[1])
        self.assertEqual('first_package', pkg.name)

if __name__ == '__main__':
    unittest.main()
