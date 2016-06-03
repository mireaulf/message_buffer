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

    def test_parse_type(self):
        t = to_cpp_test.__get_type()
        print(to_cpp.to_cpp(t))

    def test_parse_message(self):
        m = to_cpp_test.__get_message()
        print(to_cpp.to_cpp(m))

    def test_parse_package(self):
        p = package('')
        p.name = 'pkg_name'
        p.messages.append(to_cpp_test.__get_message())
        print(to_cpp.to_cpp(p))

if __name__ == '__main__':
    unittest.main()
