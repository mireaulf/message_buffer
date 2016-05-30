#!/usr/bin/python3
import unittest
from message import message

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
"""
        msg = message(stream)
        res = msg.parse()
        self.assertEqual(False, res[0])
        self.assertEqual(None, res[1])
        msg = message(stream.strip())
        res = msg.parse()
        self.assertEqual(True, res[0])
        self.assertEqual('msg_id', msg.id)
        self.assertEqual(2, len(msg.types))

if __name__ == '__main__':
    unittest.main()
