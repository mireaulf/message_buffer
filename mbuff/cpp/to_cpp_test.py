#!/usr/bin/python3
import unittest
from mbuff.parse.type import type
from mbuff.parse.message import message
from mbuff.parse.package import package
from mbuff.cpp.to_cpp import to_cpp

class to_cpp_test(unittest.TestCase):
    @staticmethod
    def __get_type():
        t = type('')
        t.name = 'name'
        t.type = 'bool'
        return t

    @staticmethod
    def __get_message():
        m = message('')
        m.id = 'msg_id'
        m.types.append(to_cpp_test.__get_type())
        return m

    @staticmethod
    def __get_package():
        p = package('')
        p.name = 'pkg_name'
        p.messages.append(to_cpp_test.__get_message())
        return p

    def test_parse_type(self):
        with self.assertRaises(ValueError):
            to_cpp.type(None, None)
        t0 = to_cpp_test.__get_type()
        with self.assertRaises(ValueError):
            to_cpp.type(t0, None)
        with self.assertRaises(ValueError):
            to_cpp.type(None, '')
        print(to_cpp.type(t0, ''))
        h0 = t0.hash
        self.assertNotEqual(h0, None)
        t1 = to_cpp_test.__get_type()
        t1.name += ' '
        to_cpp.type(t1, '')
        h1 = t1.hash
        self.assertNotEqual(h0, h1)
        t2 = to_cpp_test.__get_type()
        to_cpp.type(t2, ' ')
        h2 = t2.hash
        self.assertNotEqual(h0, h2)
        self.assertNotEqual(h1, h2)

    def test_message_parse(self):
        with self.assertRaises(ValueError):
            to_cpp.message(None, None)
        m0 = to_cpp_test.__get_message()
        with self.assertRaises(ValueError):
            to_cpp.message(m0, None)
        with self.assertRaises(ValueError):
            to_cpp.message(None, '')
        print(to_cpp.message(m0, ''))
        h0 = m0.hash
        self.assertNotEqual(h0, None)
        m1 = to_cpp_test.__get_message()
        m1.id += ' '
        to_cpp.message(m0, '')
        h1 = m1.hash
        self.assertNotEqual(h1, h0)
        m2 = to_cpp_test.__get_message()
        to_cpp.message(m2, ' ')
        h2 = m2.hash
        self.assertNotEqual(h0, h2)
        self.assertNotEqual(h1, h2)
    
    def test_package_test(self):
        with self.assertRaises(ValueError):
            to_cpp.package(None)
        p0 = to_cpp_test.__get_package()
        print(to_cpp.package(p0))
        h0 = p0.hash
        p1 = to_cpp_test.__get_package()
        to_cpp.package(p1)
        h1 = p1.hash
        self.assertEqual(h0, h1)
        p1.messages.append(to_cpp_test.__get_message())
        print(to_cpp.package(p1))
        h2 = p1.hash
        self.assertNotEqual(h0, h2)
        self.assertNotEqual(h1, h2)

if __name__ == '__main__':
    unittest.main()
