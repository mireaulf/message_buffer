#!/usr/bin/python3
import unittest
from from_stream import from_stream

class from_stream_test(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            from_stream(None, None)
        with self.assertRaises(ValueError):
            from_stream('', None)
        with self.assertRaises(TypeError):
            from_stream('', 42)
        s = from_stream('regex', '')
        self.assertEqual('regex', s.regex)
        self.assertEqual('', s.stream)

if __name__ == '__main__':
    unittest.main()
