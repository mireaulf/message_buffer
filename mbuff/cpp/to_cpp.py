#!/usr/bin/python3
from mbuff.parse.type import type as type_type
from mbuff.parse.message import message as message_type
from mbuff.parse.package import package as package_type 
import hashlib

class to_cpp:
    @staticmethod
    def type(o:type_type, hint:str):
        if o is None or hint is None:
            raise ValueError('invalid arguments')
        h = hashlib.sha256()
        h.update(o.name.encode())
        h.update(o.type.encode())
        h.update(hint.encode())
        o.hash = h.hexdigest()

    @staticmethod
    def message(o:message_type, hint:str):
        if o is None or hint is None:
            raise ValueError('invalid arguments')
        h = hashlib.sha256()
        for t in o.types:
            to_cpp.type(t, o.id)
            h.update(t.hash.encode())
        h.update(hint.encode())
        o.hash = h.hexdigest()

    @staticmethod
    def package(o:package_type):
        if o is None:
            raise ValueError('invalid arguments')
        h = hashlib.sha256()
        for m in o.messages:
            to_cpp.message(m, o.name)
            h.update(m.hash.encode())
        o.hash = h.hexdigest()
        
        
#        out = """
#// {2}
#bool m_{0}_is_set = false;
#{1} m_{0};
#public:
#void set_{0}({1} value) {{ 
#    m_{0}_is_set = true;
#    m_{0} = value; 
#}}
#{1} get_{0}() const {{
#    return m_{0};
#}}
#""".format(o.name, o.type, o.hash)
#        return out
#
#    @staticmethod
#    def message(o):
#        if not isinstance(o, message):
#            raise TypeError('Expected \'message\' type')
#        out_types = ''
#        hash = hashlib.sha256()
#        hash.update(o.id.encode())
#        for t in o.types:
#            out_types += to_cpp.type(t)
#            hash.update(t.hash.encode())
#        o.hash = hash.hexdigest()
#        out = """
#// {2}
#class {0} {{
#{1}
#}};
#""".format(o.id, out_types, o.hash)
#        return out
#
#    @staticmethod
#    def package(o):
#        if not isinstance(o, package):
#            raise TypeError('Expected \'package\' type')
#        out_msgs = ''
#        hash = hashlib.sha256()
#        hash.update(o.name.encode())
#        for msg in o.messages:
#            out_msgs += to_cpp.message(msg)
#            hash.update(msg.hash.encode())
#        o.hash = hash.hexdigest()
#        out = """
#// {2}
#namespace {0} {{
#{1}
#}}
#""".format(o.name, out_msgs, o.hash)
#        return out
"""
    @staticmethod
    def to_cpp(o):
        if isinstance(o, type):
            out = to_cpp.__to_cpp_type(o)
        elif isinstance(o, message):
            out = to_cpp.__to_cpp_message(o)
        elif isinstance(o, package):
            out = to_cpp.__to_cpp_package(o)
        else:
            raise TypeError('unknown type')
        return out
"""