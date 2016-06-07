#!/usr/bin/python3
import unittest
from parse.message import message

class message_test(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            msg = message(None)
        with self.assertRaises(TypeError):
            msg = message(42)
        msg = message('')
        msg.parse()
        self.assertNotEqual('', msg.regex)

    def test_parse(self):
        msg = message('')
        res = msg.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        stream = """ message msg_id {
    bool type_bool;
    string type_string;
};

foo bar
"""
        msg = message(stream)
        res = msg.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        msg = message(stream.strip())
        res = msg.parse()
        self.assertEqual(True, res[0])
        self.assertEqual('foo bar', res[1])
        self.assertEqual('msg_id', msg.id)
        self.assertEqual(2, len(msg.types))
        self.assertEqual('bool', msg.types[0].type)
        self.assertEqual('type_bool', msg.types[0].name)
        self.assertEqual('string', msg.types[1].type)
        self.assertEqual('type_string', msg.types[1].name)        

    def test_equals(self):
        stream = """message msg_id {
bool type0;
};"""
        msg0 = message(stream)
        msg0.parse()
        msg1 = message(stream)
        msg1.parse()
        self.assertEqual(msg0, msg1)

    def test_parse_duplicates(self):
        stream = """message msg_id {
bool type0;
bool type0;
};"""
        msg = message(stream)
        with self.assertRaises(ValueError):
            msg.parse()

if __name__ == '__main__':
    unittest.main()
