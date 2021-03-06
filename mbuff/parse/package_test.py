#!/usr/bin/python3
import unittest
from parse.package import package

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
        self.assertEqual(False, res[0])
        stream = """package foobar;

message msg_id0 {
    bool b;
};


message msg_id1 {
    int8 i;
    string str;
}; asd
"""
        pkg = package(stream)
        res = pkg.parse()
        self.assertEqual(False, res[0])
        stream = stream[:-4]
        pkg = package(stream)
        res = pkg.parse()
        self.assertEqual(True, res[0])
        self.assertEqual('', res[1])
        self.assertEqual(2, len(pkg.messages))
        self.assertEqual('msg_id0', pkg.messages[0].id)
        self.assertEqual('msg_id1', pkg.messages[1].id)

    def test_equals(self):
        stream = """package foobar;
message msg_id0 {
    bool b;
};
};"""   
        pkg0 = package(stream)
        pkg0.parse()
        pkg1 = package(stream)
        pkg1.parse()
        self.assertEqual(pkg0, pkg1)

    def test_parse_duplicates(self):
        stream = """package foobar;
message msg_id0 {
    bool b0;
};
message msg_id0 {
    bool b1;
};
};"""   
        pkg = package(stream)
        with self.assertRaises(ValueError):
            pkg.parse()

if __name__ == '__main__':
    unittest.main()
