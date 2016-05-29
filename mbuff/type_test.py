#!/usr/bin/python3
import unittest
from type import type

class type_test(unittest.TestCase):
    def parse(self, type_type):
        type_name = 'foo'
        stream = ' {0} {1}; {0} stuff '.format(type_type, type_name)
        rest = ' {0} stuff'.format(type_type)      
        t = type(stream)
        res = t.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        t = type(stream.strip())
        res = t.parse()
        print(res)
        self.assertEqual(True, res[0])
        self.assertEqual(rest, res[1])
        self.assertEqual(type_type, t.type)
        self.assertEqual(type_name, t.name)
        
    def test_init(self):
        with self.assertRaises(ValueError):
            type(None)
        with self.assertRaises(TypeError):
            type(42)
        t = type('')
        self.assertNotEqual('', t.regex)

    def test_parse(self):
        t = type('')
        res = t.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])

    def test_parse(self):        
        for t in type.types:
            self.parse(t)

if __name__ == '__main__':
    unittest.main()
