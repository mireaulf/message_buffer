#!/usr/bin/python3
from mbuff.parse.type import type
from mbuff.parse.message import message
from mbuff.parse.package import package
import hashlib

class to_cpp:
    @staticmethod
    def __to_cpp_type(o):
        o.hash = hashlib.sha256(o.name.encode() + o.type.encode()).hexdigest()
        out = """
// {2}
bool m_{0}_is_set = false;
{1} m_{0};
public:
void set_{0}({1} value) {{ 
    m_{0}_is_set = true;
    m_{0} = value; 
}}
{1} get_{0}() const {{
    return m_{0};
}}
""".format(o.name, o.type, o.hash)
        return out

    @staticmethod
    def __to_cpp_message(o):
        out_types = ''
        hash = hashlib.sha256()
        hash.update(o.id.encode())
        for t in o.types:
            out_types += to_cpp.to_cpp(t)
            hash.update(t.hash.encode())
        o.hash = hash.hexdigest()
        out = """
// {2}
class {0} {{
{1}
}};
""".format(o.id, out_types, o.hash)
        return out

    @staticmethod
    def __to_cpp_package(o):
        out_msgs = ''
        hash = hashlib.sha256()
        hash.update(o.name.encode())
        for msg in o.messages:
            out_msgs += to_cpp.to_cpp(msg)
            hash.update(msg.hash.encode())
        o.hash = hash.hexdigest()
        out = """
// {2}
namespace {0} {{
{1}
}}
""".format(o.name, out_msgs, o.hash)
        return out

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