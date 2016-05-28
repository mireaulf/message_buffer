#!/usr/bin/python3
import unittest
import re
from parsable import parsable

class parsable_test(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            parsable(None, None)
        with self.assertRaises(TypeError):
            parsable(42, None)
        with self.assertRaises(ValueError):
            parsable('', None)
        with self.assertRaises(TypeError):
            parsable('', 42)
        p = parsable('regex', '')
        self.assertEqual(re.compile('regex'), p.regex)
        self.assertEqual('', p.stream)

    def test_parse(self):
        regex = 'regex'
        p = parsable(regex, '')
        res = p.parse()
        self.assertEqual(False, res)
        p = parsable(regex, ' regex')
        res = p.parse()
        self.assertEqual(False, res)
        stream = ' regex; asd '
        p = parsable(regex, stream)
        res = p.parse()
        self.assertEqual(False, res)
        p = parsable(regex, stream.strip())
        res = p.parse()
        self.assertEqual(True, res)

if __name__ == '__main__':
    unittest.main()
